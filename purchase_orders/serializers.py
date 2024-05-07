from rest_framework import serializers  
from .models import PurchaseOrders
from vendors.models import Vendors
import datetime
from datetime import timezone
import logging 
from rest_framework.response import Response
from rest_framework import status
import random 
import string
from vendor_performance.performance_metrics import generatePerformanceMetrics 

logger = logging.getLogger(__name__)

class PurchaseOrdersSerializer(serializers.ModelSerializer):
    po_number = serializers.CharField(required=False) 
    vendor = serializers.CharField()
    order_date = serializers.DateTimeField() 
    delivery_date = serializers.DateTimeField()  
    items = serializers.JSONField() 
    quantity = serializers.IntegerField() 
    status = serializers.CharField()  
    quality_rating = serializers.FloatField(required=False)  
    issue_date = serializers.DateTimeField(required=False) 
    acknowledgment_date = serializers.DateTimeField(required=False)
    order_completed_date = serializers.DateTimeField(required=False)

    vendor = serializers.PrimaryKeyRelatedField(queryset=Vendors.objects.all(),many=False)

    class Meta:
        model = PurchaseOrders
        fields = ('__all__')

    # Create and return a new `PurchaseOrders` instance, given the validated data.
    def create(self, validateData):
        # validateData['po_number'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        purchase_order = PurchaseOrders.objects.create(**validateData)
        generatePerformanceMetrics(purchase_order)
        return purchase_order

    # Update and return an existing `PurchaseOrders` instance, given the validated data.
    def update(self, instance, validatedData):
        try:
            instance.po_number = validatedData.get('po_number', instance.po_number)
            instance.vendor = validatedData.get('vendor', instance.vendor)
            instance.order_date = validatedData.get('order_date', instance.order_date)
            instance.delivery_date = validatedData.get('delivery_date', instance.delivery_date)
            instance.items = validatedData.get('items', instance.items)
            instance.quantity = validatedData.get('quantity', instance.quantity)
            instance.status = validatedData.get('status', instance.status)
            instance.quality_rating = validatedData.get('quality_rating', instance.quality_rating)
            instance.issue_date = validatedData.get('issue_date', instance.issue_date)
            instance.acknowledgment_date = validatedData.get('acknowledgment_date', instance.acknowledgment_date)

            if instance.status == 'completed':
                instance.order_completed_date = datetime.datetime.now(timezone.utc) 

            instance.save()

            # vendorPerfomanceModelInstance, created =  VendorPerformanceModel.objects.get_or_create(vendor=instance.vendor)
            
            # # Performance Metrics 1.   On-Time Delivery Rate & Quality Rating Average
            # # Logic for updating metrics in vendor perfomance model if status is 'completed'
            
            # if instance.status == 'completed':
            #     with transaction.atomic():
                    
            #         if instance.order_completed_date <= instance.delivery_date:
            #             vendorPerfomanceModelInstance.on_time_delivered_orders += 1
                    
            #         vendorPerfomanceModelInstance.total_completed_orders += 1                           # Every time order is completed increase by one
            #         vendorPerfomanceModelInstance.total_quality_rating += instance.quality_rating       # Every time order is completed increase by current rating

            #         #  Calculate on_time_delivery_rate (completedPOsOnTime / totalCompltedPOs).
            #         vendorPerfomanceModelInstance.on_time_delivery_rate = vendorPerfomanceModelInstance.on_time_delivered_orders / vendorPerfomanceModelInstance.total_completed_orders
                    
            #         # Calculate quality_rating_avg = (totalQualityRating / totalCompletedOrders)
            #         vendorPerfomanceModelInstance.quality_rating_avg = vendorPerfomanceModelInstance.total_quality_rating / vendorPerfomanceModelInstance.total_completed_orders
                    
            #         vendorPerfomanceModelInstance.save()


            # # Performance Metrics 3. CALCULATE AVERAGE RESPONSE TIME

            # if instance.acknowledgment_date:
            #     vendorPerfomanceModelInstance.average_response_time = 9.1
            



            # # Performance Metrics 4.  FULFILMENT RATE
            # """
            # FORMULA :   fulfillment_rate = completedPOsOnTime / totalIssuedPOs 

            # Assuming that PO is issued to the vendor as soon as PO is generated in the system ,
            # so the totalIssuedPOs is equal to the POs exist in the system
            # """
            # # Calculated upon any change in PO status (EVERY TIME). 
            # if instance.status:     
            #     totalIssuedPOs = len(PurchaseOrders.objects.all())
            #     vendorPerfomanceModelInstance.fulfillment_rate = vendorPerfomanceModelInstance.total_completed_orders / totalIssuedPOs
            #     vendorPerfomanceModelInstance.save()
            
            generatePerformanceMetrics(instance, validatedData.get('acknowledgment_date', False))
            
            return instance
        except Exception as e:
            logger.error(f'Error in updating PO instance: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# instance.vendor = validateData.get('vendor', instance.vendor)
# instance.date = validateData.get('date', instance.date)
# instance.on_time_delivery_rate = validateData.get('vendor', instance.vendor)     
# instance.quality_rating_avg = validateData.get('on_time_delivery_rate', instance.on_time_delivery_rate)    
# instance.average_response_time = validateData.get('average_response_time', instance.average_response_time)     
# instance.average_response_time =


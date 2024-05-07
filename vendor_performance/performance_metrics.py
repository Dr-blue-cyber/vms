from .models import VendorPerformanceModel
from purchase_orders.models import PurchaseOrders
from vendors.models import Vendors
from django.db import transaction


def generatePerformanceMetrics(instance, flag = False):
    vendorInstance = Vendors.objects.get(id=instance.vendor.id)
    vendorPerfomanceModelInstance, created =  VendorPerformanceModel.objects.get_or_create(vendor=instance.vendor)
            
    # Performance Metrics 1.   On-Time Delivery Rate & Quality Rating Average
    # Logic for updating metrics in vendor perfomance model if status is 'completed'
    
    if instance.status == 'completed':
        with transaction.atomic():
            
            if instance.order_completed_date <= instance.delivery_date:
                vendorPerfomanceModelInstance.on_time_delivered_orders += 1
            
            vendorPerfomanceModelInstance.total_completed_orders += 1                           # Every time order is completed increase by one
            if instance.quality_rating:
                vendorPerfomanceModelInstance.total_quality_rating += instance.quality_rating       # Every time order is completed increase by current rating

            #  Calculate on_time_delivery_rate (completedPOsOnTime / totalCompltedPOs).
            vendorPerfomanceModelInstance.on_time_delivery_rate = vendorPerfomanceModelInstance.on_time_delivered_orders / vendorPerfomanceModelInstance.total_completed_orders
            
            # Calculate quality_rating_avg = (totalQualityRating / totalCompletedOrders)
            vendorPerfomanceModelInstance.quality_rating_avg = vendorPerfomanceModelInstance.total_quality_rating / vendorPerfomanceModelInstance.total_completed_orders

            # Add quality_rating_avg, on_time_delivery_rate in Vendors Model
            vendorInstance.quality_rating_avg = vendorPerfomanceModelInstance.quality_rating_avg
            vendorInstance.on_time_delivery_rate = vendorPerfomanceModelInstance.on_time_delivery_rate

            vendorInstance.save()
            vendorPerfomanceModelInstance.save()


    # Performance Metrics 3. CALCULATE AVERAGE RESPONSE TIME

    # FORMULA: AVG (issued_date - acknowledgment_date)

    # update the average_response_time only on first time of acknowledgment_date updated
    if flag and instance.acknowledgment_date :
        vendorPerfomanceModelInstance.total_acknowledgment_po_s += 1 
        vendorPerfomanceModelInstance.total_response_time += (instance.acknowledgment_date - instance.issue_date).total_seconds()
        vendorPerfomanceModelInstance.average_response_time = vendorPerfomanceModelInstance.total_response_time / vendorPerfomanceModelInstance.total_acknowledgment_po_s

        # Add average_response_time in Vendors Model
        vendorInstance.average_response_time = vendorPerfomanceModelInstance.average_response_time

        vendorInstance.save()

        vendorPerfomanceModelInstance.save()
    



    # Performance Metrics 4.  FULFILMENT RATE
    """
    FORMULA :   fulfillment_rate = completedPOsOnTime / totalIssuedPOs 

    Assuming that PO is issued to the vendor as soon as PO is generated in the system ,
    so the totalIssuedPOs is equal to the POs exist in the system
    """
    # Calculated upon any change in PO status (EVERY TIME). 
    if instance.status:     
        totalIssuedPOs = len(PurchaseOrders.objects.all())
        vendorPerfomanceModelInstance.fulfillment_rate = vendorPerfomanceModelInstance.total_completed_orders / totalIssuedPOs

        # Add fulfillment_rate in Vendors Model
        vendorInstance.fulfillment_rate = vendorPerfomanceModelInstance.fulfillment_rate

        vendorInstance.save()
        vendorPerfomanceModelInstance.save()
    
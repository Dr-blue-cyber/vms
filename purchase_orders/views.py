from django.shortcuts import render
from .models import PurchaseOrders
from .serializers import PurchaseOrdersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404  
import logging 
from vendor_performance.performance_metrics import generatePerformanceMetrics 
import random 
import string


logger = logging.getLogger(__name__)
# Create your views here.

class PurchaseOrderView(APIView):
    def get(self,request, id=None):
        try:
            vendor_id = request.query_params.get('vendor')
            if vendor_id:   # Filter purchase orders by vendor
                result = PurchaseOrders.objects.filter(vendor=vendor_id)
                serializers = PurchaseOrdersSerializer(result, many=True)
                return Response({'status': 'success', 'purchase_order': serializers.data, 'message': "Get all filtered"})

            if id is not None:
                result = PurchaseOrders.objects.get(id=id)
                serializers = PurchaseOrdersSerializer(result)
                return Response({'status': 'success', "purchase_order": serializers.data}, status=200)

            result = PurchaseOrders.objects.all()
            serializers = PurchaseOrdersSerializer(result, many=True)
            return Response({'status': 'success', "purchase_orders": serializers.data}, status=200)
        except Exception as e:
            logger.error(f'Error in PO GET: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self,request):
        try:
            # Generate a unique po_number at runtime to ensure user-friendly system identification
            request.data['po_number'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            serializers = PurchaseOrdersSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({'status':'success', 'data': serializers.data},status=status.HTTP_200_OK,)
            else:
                return Response({'status':'error', 'data': serializers.errors},status=status.HTTP_400_BAD_REQUEST,)
        except Exception as e:
            logger.error(f'Error in PO POST: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def patch(self, request, id):
        try:
            result = PurchaseOrders.objects.get(id=id)
            serializer = PurchaseOrdersSerializer(result, data = request.data, partial=True)
            # generatePerformanceMetrics(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": 'success', 'data': serializer.data}, )
            else:
                return Response({"status": 'error', 'data': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR )
        except Exception as e:
            logger.error(f'Error in PO PATCH: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # will automatically return the 404 error if the given id is not present.
    def delete(self, request, id=None): 
        try: 
            result = get_object_or_404(PurchaseOrders, id=id)  
            result.delete()  
            return Response({"status": "success", "data": "Record Deleted"})
        except Exception as e:
            logger.error(f'Error in PO DELETE: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)








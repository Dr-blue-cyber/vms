from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import VendorPerformanceModel
from .serializer import VendorPerformanceSerializer

import logging 

logger = logging.getLogger(__name__)

# Create your views here.
class VendorPerformanceView(APIView):

    def get(self, request):
        try:
            vendor_id = request.query_params.get('vendor')
            if vendor_id: 
                result = VendorPerformanceModel.objects.filter(vendor=vendor_id)
                serializers = VendorPerformanceSerializer(result, many=True)
                return Response({'status': 'success', 'vendor_performance': serializers.data, 'message': "Get all filtered"})

            if id is not None:
                result = VendorPerformanceModel.objects.get(id=id)
                serializers = VendorPerformanceSerializer(result)
                return Response({'status': 'success', "vendor_performance": serializers.data}, status=200)

            result = VendorPerformanceModel.objects.all()
            serializers = VendorPerformanceSerializer(result, many=True)
            return Response({'status': 'success', "vendor_performances": serializers.data}, status=200)
       
        except Exception as e:
            logger.error(f'Error in vendor perfomace GET: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            pass
        except Exception as e:
            logger.error(f'Error in vendor perfomace POST: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        try:
            pass
        except Exception as e:
            logger.error(f'Error in vendor perfomace PATCH: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            pass
        except Exception as e:
            logger.error(f'Error in vendor perfomace DELETE: {e}')
            return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Vendors
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VendorsSerializer, VendorPerformanceSerializer
from django.shortcuts import get_object_or_404 
import logging 
import random 
import string

from django.utils.decorators import method_decorator
from vms.auth_middleware import check_api_key

logger = logging.getLogger(__name__)


# Create your views here.
  
# class based view

@method_decorator(check_api_key, name='dispatch')
class VendorsView(APIView):
    
        # def get(self, request, id, *args, **kwargs):
        def get(self, request, id=None):
            try:
                if id is not None: 
                    result = Vendors.objects.get(id=id) 
                    serializers = VendorsSerializer(result)
                    return Response({'status': 'success', "vendor": serializers.data}, status=200)
                
                result = Vendors.objects.all() 
                serializers = VendorsSerializer(result, many=True)
                return Response({'status': 'success', "vendors": serializers.data}, status=200)
            
            except Exception as e:
                logger.error(f'Error in GET: {e}')
                return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        def post(self,request):
            try:
                # Generate a unique vendor code at runtime to ensure user-friendly system identification
                request.data['vendor_code'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

                serializers = VendorsSerializer(data=request.data)
                if serializers.is_valid():
                    serializers.save()
                    return Response({'status':'success', 'data': serializers.data},status=status.HTTP_200_OK,)
                else:
                    return Response({'status':'error', 'data': serializers.errors},status=status.HTTP_400_BAD_REQUEST,)
            except Exception as e:
                logger.error(f'Error in POST: {e}')
                return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        def patch(self, request, id):
            try:
                result = Vendors.objects.get(id=id)
                serializer = VendorsSerializer(result, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": 'success', 'data': serializer.data}, )
                else:
                    return Response({"status": 'error', 'data': serializer.errors}, )
            except Vendors.DoesNotExist:
                return Response({'status': 'error', 'data': 'Vendor not found.'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                logger.error(f'Error in PATCH: {e}')
                return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

        # will automatically return the 404 error if the given id is not present.
        def delete(self, request, id=None):  
            try:
                result = get_object_or_404(Vendors, id=id)  
                result.delete()  
                return Response({"status": "success", "data": "Record Deleted"})
            except Exception as e:
                logger.error(f'Error in DELETE: {e}')
                return Response({'status': 'error', 'data': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



@method_decorator(check_api_key, name='dispatch')
class VendorPerformanceView(APIView):
    def get(self, request, id):
        try:
           # Retrieve the vendor
            result = Vendors.objects.filter(id=id).values('on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
            if result:
                serializers = VendorPerformanceSerializer(result, many=True)  # If handling multiple objects
                return JsonResponse({'status': 'success', 'data': serializers.data}, status=200)
            else:
                return JsonResponse({'status': 'error', 'data': 'No matching records found'}, status=404)
        except Vendors.DoesNotExist:
            return JsonResponse({'status': 'error', 'data': 'Vendor not found.'}, status=404)
        except Exception as e:
            logger.error(f'Error in GET performance: {e}')
            return JsonResponse({'status': 'error', 'data': str(e)}, status=500)









# to avoid CSRF exception
@csrf_exempt
def vendors(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            name = body.get("name")
            contact_details = body.get("contact_details") 
            address =  body.get("address")
            vendor_code =  body.get("vendor_code") 
            on_time_delivery_rate =  body.get("on_time_delivery_rate") 
            quality_rating_avg =  body.get("quality_rating_avg") 
            average_response_time =  body.get("average_response_time") 
            fullfillment_rate =  body.get("fullfillment_rate") 
                
            new_vendor = Vendors.objects.create(name= name, contact_details=contact_details,address=address, vendor_code=vendor_code,
                                                on_time_delivery_rate=on_time_delivery_rate,quality_rating_avg=quality_rating_avg,
                                                average_response_time=average_response_time,fullfillment_rate=fullfillment_rate)
            
            return JsonResponse({"message": "user added succesfully"}, status= 201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status= 201)

    if request.method == "GET":
        logger.error(request)
        result = Vendors.objects.all()
        serializer = VendorsSerializer(result, many='True')
        return JsonResponse({'status': 'success', 'data': serializer.data}, status= 200)
  
from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Vendors
# from .serializers import VendorsSerializer

from django.http import JsonResponse
from .models import Vendors
from django.views.decorators.csrf import csrf_exempt
import json




# Create your views here.

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
        # get all vendor login
        print(request)
        return HttpResponse("Hello woorld.")
    
    
# class based view

# class VendorsView(APIView):

#     def get(self, request, *args, **kwargs):
#         result = Vendors.objects.all() 
#         serializers = VendorsSerializer(result, many=True)
#         return Response({'status': 'success', "students": serializers.data}, status=200)
    
#     def post(self,request):
#         serializers = VendorsSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response({'status':'success', 'data': serializers.data},status=status.HTTP_200_OK,)
#         else:
#             return Response({'status':'error', 'data': serializers.error},status=status.HTTP_400_BAD_REQUEST,)

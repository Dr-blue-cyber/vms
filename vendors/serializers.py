from rest_framework import serializers  
from .models import Vendors

class VendorsSerializer(serializers.ModelSerializers):
    name = serializers.CharField(max_length=100) 
    contact_details = serializers.TextField() 
    address = serializers.TextField() 
    vendor_code = serializers.CharField()
    on_time_delivery_rate = serializers.FloatField(default= False) 
    quality_rating_avg = serializers.FloatField() 
    average_response_time = serializers.FloatField() 
    fullfillment_rate = serializers.FloatField()

    class Meta:
        model = Vendors
        fields = ('__all__')

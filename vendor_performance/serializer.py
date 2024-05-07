from rest_framework import serializers  
from .models import Vendors
from .models import VendorPerformanceModel

class VendorPerformanceSerializer(serializers.ModelSerializer):
    vendor =  serializers.CharField()
    date = serializers.DateTimeField(required=False)
    on_time_delivery_rate = serializers.FloatField()     
    quality_rating_avg = serializers.FloatField()    
    average_response_time = serializers.FloatField()     
    fulfillment_rate = serializers.FloatField()      

    vendor = serializers.PrimaryKeyRelatedField(queryset=Vendors.objects.all(),many=False)

    class Meta:
        model = VendorPerformanceModel
        fields = ('__all__')
    
    # Create and return a new `VendorPerformanceModel` instance, given the validated data.
    def create(self, validateData):
        vendor_performance = VendorPerformanceModel.objects.create(**validateData)
        return vendor_performance
    
    def update(self, instance, validateData):
        instance.vendor = validateData.get('vendor', instance.vendor)
        instance.date = validateData.get('date', instance.date)
        instance.on_time_delivery_rate = validateData.get('vendor', instance.vendor)     
        instance.quality_rating_avg = validateData.get('on_time_delivery_rate', instance.on_time_delivery_rate)    
        instance.average_response_time = validateData.get('average_response_time', instance.average_response_time)     
        instance.fulfillment_rate = validateData.get('fulfillment_rate', instance.fulfillment_rate)  

        instance.save()
        return instance
    
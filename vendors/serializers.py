from rest_framework import serializers  
from .models import Vendors

class VendorsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100) 
    contact_details = serializers.CharField() 
    address = serializers.CharField() 
    vendor_code = serializers.CharField(required=False)
    on_time_delivery_rate = serializers.FloatField(required=False) 
    quality_rating_avg = serializers.FloatField(required=False) 
    average_response_time = serializers.FloatField(required=False) 
    fullfillment_rate = serializers.FloatField(required=False)

    class Meta:
        model = Vendors
        fields = ('__all__')

    # Create and return a new `Vendors` instance, given the validated data.
    def create(self, validateData):
        return Vendors.objects.create(**validateData)

    # Update and return an existing `Vendors` instance, given the validated data.
    def update(self, instance, validatedData):
        instance.name = validatedData.get('name', instance.name)
        instance.contact_details = validatedData.get('contact_details', instance.contact_details)
        instance.address = validatedData.get('address', instance.address)
        instance.vendor_code = validatedData.get('vendor_code', instance.vendor_code)
        instance.on_time_delivery_rate = validatedData.get('on_time_delivery_rate', instance.on_time_delivery_rate)
        instance.quality_rating_avg = validatedData.get('quality_rating_avg', instance.quality_rating_avg)
        instance.average_response_time = validatedData.get('average_response_time', instance.average_response_time)
        instance.fullfillment_rate = validatedData.get('fullfillment_rate', instance.fullfillment_rate)

        instance.save()
        return instance


class VendorPerformanceSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.FloatField(required=False) 
    quality_rating_avg = serializers.FloatField(required=False) 
    average_response_time = serializers.FloatField(required=False) 
    fulfillment_rate = serializers.FloatField(required=False)

    class Meta:
        model = Vendors
        fields = ('on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate')
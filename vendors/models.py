from django.db import models

# Create your models here.
class Vendors(models.Model):
    name = models.CharField(max_length=100) 
    contact_details = models.TextField() 
    address = models.TextField()
    vendor_code = models.CharField(max_length=100)
    on_time_delivery_rate = models.FloatField( null=True)  # None because when vendor created we dont have there perfomance metrics
    quality_rating_avg = models.FloatField( null=True) 
    average_response_time = models.FloatField(null=True) 
    fulfillment_rate = models.FloatField(null=True)

    # class Meta:
    #     verbose_name_plural = "Vendors"


    # return objects in human readable form
    def __str__(self) -> str:
        return self.name
    
    
from django.db import models

# Create your models here.
class Vendors(models.Model):
    name = models.CharField(max_length=100) 
    contact_details = models.TextField() 
    address = models.TextField()
    vendor_code = models.CharField(max_length=100)
    on_time_delivery_rate = models.FloatField(default= False) 
    quality_rating_avg = models.FloatField() 
    average_response_time = models.FloatField() 
    fullfillment_rate = models.FloatField()

    # class Meta:
    #     verbose_name_plural = "Vendors"

    # def __str__(self) -> str:
    #     return self.name
    
    
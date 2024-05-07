from django.db import models
from vendors.models import Vendors

# Create your models here.
class VendorPerformanceModel(models.Model):
    vendor =  models.ForeignKey(Vendors, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)                      # Date of the performance record.
    on_time_delivery_rate = models.FloatField(null=True)            # Historical record of the on-time delivery rate.
    quality_rating_avg = models.FloatField(null=True)               # Historical record of the quality rating average.
    average_response_time = models.FloatField(null=True)            # Historical record of the average response
    fulfillment_rate = models.FloatField(null=True)                 # Historical record of the fulfilment rate.
    on_time_delivered_orders = models.IntegerField(default=0)       # number of orders delivered on time.
    total_completed_orders = models.IntegerField(default=0)         # total completed deals till now.
    total_quality_rating = models.IntegerField(default=0)           # total quality ratings of vendors till now.
    total_acknowledgment_po_s = models.IntegerField(default=0)         # total completed deals till now.
    total_response_time = models.IntegerField(default=0)           # total quality ratings of vendors till now.

    def __str__(self) -> str:
        return f'vendor: {self.vendor}'
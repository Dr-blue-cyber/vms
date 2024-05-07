from django.db import models
from vendors.models import Vendors

# Create your models here.
class PurchaseOrders(models.Model):
    po_number =  models.CharField(max_length=100,blank=True)                        # Unique number identifying the PO.
    vendor =  models.ForeignKey(Vendors, on_delete=models.CASCADE)      # Link to the Vendor model.
    order_date =  models.DateTimeField()                                 # Date when the order was placed.
    delivery_date =  models.DateTimeField()                              # Expected or actual delivery date of the order.
    items =  models.JSONField()                                         # Details of items ordered.
    quantity =  models.IntegerField()                                    # Total quantity of items in the PO.
    status =  models.CharField(max_length=100)                           # Current status of the PO (e.g., pending, completed, canceled).
    quality_rating =  models.FloatField(null=True, blank=True)                       #  Rating given to the vendor for this PO
    issue_date =  models.DateTimeField(auto_now_add=True, blank=True)                # Timestamp when the PO was issued to the vendor.
    acknowledgment_date =  models.DateTimeField(null=True, blank=True)       # Timestamp when the vendor acknowledged the PO.
    order_completed_date =  models.DateTimeField(null=True,blank=True)            # Timestamp when order is completed.

    def __str__(self) -> str:
        return f'PO: {self.po_number}'
    
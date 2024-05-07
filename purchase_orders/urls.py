from django.urls import path
from .views import PurchaseOrderView
from vms.auth_middleware import api_key_required

urlpatterns = [
    path('', api_key_required(PurchaseOrderView.as_view()), name='PurchaseOrders'),
    path('<int:id>/', api_key_required(PurchaseOrderView.as_view()), name='PurchaseOrders'),
]
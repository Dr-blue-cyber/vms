from django.urls import path
from .views import PurchaseOrderView

urlpatterns = [
    path('', PurchaseOrderView.as_view(), name='PurchaseOrders'),
    path('<int:id>/', PurchaseOrderView.as_view(), name='PurchaseOrders'),
]
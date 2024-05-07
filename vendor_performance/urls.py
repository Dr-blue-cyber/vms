from django.urls import path
from .views import VendorPerformanceView
from vms.auth_middleware import api_key_required

urlpatterns = [
    path('', api_key_required(VendorPerformanceView.as_view()), name='VendorPerformance'),
    path('<int:id>/', api_key_required(VendorPerformanceView.as_view()), name='VendorPerformance'),
]
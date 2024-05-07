from django.urls import path
from .views import vendors
from . import views
from vms.auth_middleware import api_key_required
from .views import VendorsView, VendorPerformanceView


urlpatterns = [
    # path('', views.vendors, name='vendors'),
    path('', api_key_required(VendorsView.as_view()), name='vendors'),
    path('<int:id>/', api_key_required(VendorsView.as_view()), name='vendors'),
    path('<int:id>/performance/', api_key_required(VendorPerformanceView.as_view()), name='vendor_performance'),
]
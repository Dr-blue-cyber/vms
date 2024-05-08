from django.urls import path
from . import views
from .views import VendorsView, VendorPerformanceView

urlpatterns = [
    # path('', views.vendors, name='vendors'),
    path('', VendorsView.as_view(), name='vendors'),
    path('<int:id>/', VendorsView.as_view(), name='vendors'),
    path('<int:id>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
]
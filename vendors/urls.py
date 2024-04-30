from django.urls import path
from .views import vendors
from . import views
urlpatterns = [
    path('', views.vendors, name='vendors'),
    # path('', VendorsView.as_view(), name='vendors'),
]
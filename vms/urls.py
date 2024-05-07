"""
URL configuration for vms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .view import return_json

from django.http import JsonResponse
from vendors.views import VendorsView

def api_key_required(view_func):
    def wrapped(request, *args, **kwargs):
        # Retrieve API key from request headers or query parameters
        api_key = request.headers.get('x-api-key') or request.GET.get('api_key')
        
        # Validate the API key
        if api_key != 'secretKey':  # Replace 'YOUR_API_KEY' with your actual API key
            return JsonResponse({'error': 'Invalid API Key'}, status=403)
        
        # Call the view function if the API key is valid
        return view_func(request, *args, **kwargs)
    return wrapped


urlpatterns = [
    path('', return_json, name='base_url'),
    path('admin/', admin.site.urls),
    path('api/vendors/', include('vendors.urls')),  # vendor app routing
    path('api/purchase_orders/', include('purchase_orders.urls'))
]

# username: suraj
# password: suraj
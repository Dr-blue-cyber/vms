from functools import wraps
from django.http import JsonResponse

SECRET_KEY = 'secretKey'  # better to store sensitive information in .env file

def check_api_key(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        
        
        # Get the API key from the request headers
        api_key = request.headers.get('x-api-key')
        
        # Check if the API key is valid
        if api_key != SECRET_KEY:
            return JsonResponse({'error': 'Invalid API key'}, status=403)
        
        # If the API key is valid, proceed to the view
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view



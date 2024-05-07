
from django.http import JsonResponse

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
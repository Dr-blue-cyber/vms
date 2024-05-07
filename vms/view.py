from django.http import JsonResponse

def return_json(request):
    data = {
        "_v": "0.0.0"
    }
    return JsonResponse(data)
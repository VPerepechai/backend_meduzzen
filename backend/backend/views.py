from django.http import JsonResponse
from django.core.cache import cache

def health_check(request):
    response_data = {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }
    return JsonResponse(response_data)


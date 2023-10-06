from django.http import JsonResponse
from django.core.cache import cache

def health_check(request):
    response_data = {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }
    return JsonResponse(response_data)

def cache_view(request):
    # Set a value into the cache
    cache.set('my_key', 'my_value', 5)  # Cache for 5 seconds
    # Get a value from the cache
    my_value = cache.get('my_key')
    response_data = {
        "my_key": my_value
    }

    return JsonResponse(response_data)

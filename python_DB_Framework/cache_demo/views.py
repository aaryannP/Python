from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time

# Cache the output of this view for 15 minutes (900 seconds)
@cache_page(60 * 15)
def expensive_view(request):
    """
    A simulated expensive view that gets cached.
    """
    # Simulate an expensive database query or calculation
    time.sleep(2)
    current_time = timezone.now()
    return HttpResponse(f"<h1>Expensive operation finished.</h1><p>Time calculated: {current_time}</p>")

def manual_cache_view(request):
    """
    Manually set and get a value from the cache.
    """
    # Check if we have 'my_custom_key' in the cache
    cached_data = cache.get('my_custom_key')
    
    if cached_data is None:
        # If not, generate it and store it in cache for 60 seconds
        cached_data = f"Manually generated data at {timezone.now()}"
        cache.set('my_custom_key', cached_data, 60)
        source = "Freshly generated"
    else:
        source = "Retrieved from Memcached"

    return JsonResponse({'source': source, 'data': cached_data})

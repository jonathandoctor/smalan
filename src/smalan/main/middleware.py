from django.conf import settings
from django.http import HttpResponseForbidden

class AdminLockMiddleware(object):
    def process_request(self, request):
        """Keeps ips not in ADMIN_IPS out of /admin."""
        if request.META['REMOTE_ADDR'] in settings.ADMIN_IPS:
            return
        if request.path.startswith('/'):
            return HttpResponseForbidden('403 Forbidden')
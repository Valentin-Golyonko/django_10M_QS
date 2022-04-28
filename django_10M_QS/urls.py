import logging

from django.contrib import admin
from django.urls import path, include

from django_10M_QS.settings import DEBUG

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', include('some_app.urls')),
    path('admin/', admin.site.urls),
]

if DEBUG:
    try:
        import debug_toolbar

        urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    except Exception as ex:
        logger.error(f"config urls: {ex = }")

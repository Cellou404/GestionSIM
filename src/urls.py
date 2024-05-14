
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("simcards/", include("simcard.urls")),
    path("devices/", include("devices.urls")),
]

# The following two lines use the static() function to serve static and media files
# during development. These lines should be removed in a production environment.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
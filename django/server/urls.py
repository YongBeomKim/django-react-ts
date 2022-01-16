# https://docs.djangoproject.com/en/4.0/topics/http/urls/
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]


# Django DEBUG Tools & Media Folders
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
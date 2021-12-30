#https://docs.djangoproject.com/en/3.2/topics/http/urls/
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
from .views import Index
import debug_toolbar


# React Site regex (\b = boundary)
url_re = r'^\b(test|main/2[\d]{3})\b/$'


# User Customized Urls
urlpatterns = [
    path('admin/', admin.site.urls),   # Admin & DRF Urls
    path('', Index.as_view()),         # React Home
    re_path(url_re, Index.as_view()),  # React Routers
]


# Django DEBUG Tools & Media Folders
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
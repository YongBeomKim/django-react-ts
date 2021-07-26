from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
import debug_toolbar
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import IndexView, json_api, json_api_day

# User Customized Urls
urlpatterns = [
    path("api-word/", json_api),
    path("api-word/<int:pk>/", json_api_day),
    path('', IndexView.as_view(), name="home"),
    re_path(r"\b(create_word|day|day/[0-9]+)\b/", IndexView.as_view()),
]

# Admin & DRF Urls
urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Django DEBUG Tools & Media Folders
if settings.DEBUG:

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

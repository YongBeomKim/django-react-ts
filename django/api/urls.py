from django.urls import path, re_path
from .views import Index


# React Site regex (\b = boundary)
url_re = r'^\b(home|main/[\d]{1,3})\b/$'
urlpatterns = [
    path('', Index.as_view()),           # React Home
    re_path(url_re, Index.as_view()),    # React Routers    
]
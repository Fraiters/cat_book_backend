from django.urls import path, include
from .views import *


urlpatterns = [
    path(r'registration/', include('djoser.urls')),  # (+ users/)
    path(r'', include('djoser.urls.authtoken')),  # (+ token/login | logout)
    path(r'user/by/token/', UserByTokenApi.as_view()),
]

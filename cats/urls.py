from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path(r'cat_list/', CatsApiList.as_view(), name='cat_list'),
    path(r'add_cat/', CatsApiCreate.as_view(), name='add_cat'),
    path(r'<int:pk>/', CatsApiRetrieve.as_view(), name='cat_id'),
    path(r'<int:pk>/upd_cat/', CatsApiUpdate.as_view(), name='upd_cat'),
    path(r'<int:pk>/del_cat/', CatsApiDestroy.as_view(), name='del_cat'),
    re_path(r'^auth/register/', include('djoser.urls')),
]

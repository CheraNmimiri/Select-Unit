from django.urls import path
from .views import *


urlpatterns = [
    path("", StudentList.as_view(), name='homepage'),
    path("information/<uuid:pk>", StudentDetail.as_view(), name='information'),
]

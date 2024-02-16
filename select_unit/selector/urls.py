from django.urls import path
from .views import *

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("register/", Register.as_view(), name='register'),
    path("login/", Login.as_view(), name ="login"),
    path("information/<uuid:pk>", StudentDetail.as_view(), name='student-detail'),
    path("home_admin", LessoneList.as_view(), name = "home-admin"),
    path("lessone_detail/<int:pk>", LessoneDetail.as_view(), name ="lessone-datail"),
]

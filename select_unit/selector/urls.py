from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("register/", Register.as_view(), name='register'),
    path("login/", Login.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='home'), name="logout"),
    path("information/<uuid:pk>", StudentDetail.as_view(), name='student-detail'),
    path("home_admin", LessonList.as_view(), name="home-admin"),
    path("lessone_detail/<int:pk>", LessonDetail.as_view(), name="lesson-detail"),
]

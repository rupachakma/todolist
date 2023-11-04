
from django.urls import path

from base import views

urlpatterns = [
    path('', views.signuppage,name="signuppage"),
    path('loginpage', views.loginpage,name="loginpage"),
    path('homepage', views.homepage,name="homepage"),
]

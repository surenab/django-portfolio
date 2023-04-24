from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name="generator-home"),
    path('password/', views.password, name="password"),
    path('about/', views.about, name="about"),
]

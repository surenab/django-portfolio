from django.urls import path
from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("project-detail/<int:project_id>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),
]

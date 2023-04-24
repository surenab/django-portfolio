from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.all_blogs, name="all_blogs"),
    path("show-pdf/", views.show_pdf, name="show_pdf"),
    path("<int:blog_id>/", views.detail, name="detail"),
]

# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/<int:pk>/comment/", views.add_comment, name="add_comment"),
]

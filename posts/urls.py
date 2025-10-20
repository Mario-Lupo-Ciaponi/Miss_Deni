from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.NewsListView.as_view(), name="news"),
    path("add-post/", views.AddPostView.as_view(), name="add-post"),
]
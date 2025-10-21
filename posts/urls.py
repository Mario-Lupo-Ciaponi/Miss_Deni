from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.NormalPostListView.as_view(), name="posts"),
    path("news/", views.NewsListView.as_view(), name="news"),
    path("add-post/", views.AddPostView.as_view(), name="add-post"),
    path("<int:pk>/", include([
        path("edit-post/", views.EditPostView.as_view(), name="edit-post"),
        path("delete-post/", views.DeletePostView.as_view(), name="delete-post"),
    ])),

]
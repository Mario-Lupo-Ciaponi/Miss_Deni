from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("search-parents/", views.SearchParentView.as_view(), name="search-parents"),
    path("admin-panel/", views.AdminPanelView.as_view(), name="admin-panel"),
]
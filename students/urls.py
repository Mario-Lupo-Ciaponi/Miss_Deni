from django.urls import path, include
from . import views

urlpatterns = [
    path("groups/", include([
        path("create/", views.CreateFormView.as_view(), name="create-group"),
        path("<int:pk>/", include([
           path("update/", views.UpdateFormView.as_view(), name="update-view"),
        ]))
    ])),
]

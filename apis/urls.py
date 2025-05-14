from django.urls import path, include

from .views import TaskListCreateAPIView, TaskUpdateDeleteView

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("tasks/", TaskListCreateAPIView.as_view()),
    path("tasks/<int:pk>/", TaskUpdateDeleteView.as_view()),
]

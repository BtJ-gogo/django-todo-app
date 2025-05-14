from django.urls import path
from .views import (
    TaskListView,
    TaskDeleteView,
    TaskCreateView,
    TaskUpdateView,
    toggle_task_status,
    completed_tasks_delete,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"),
    path("toggle/<int:pk>/", toggle_task_status, name="task_toggle"),
    path(
        "delete-completed-task/", completed_tasks_delete, name="completed_tasks_delete"
    ),
]

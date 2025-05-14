from rest_framework.generics import (
    ListCreateAPIView,
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from .serializers import TodoSerializer
from todo_app.models import Todo


class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


"""
class TaskUpdateDeleteView(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""


class TaskUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

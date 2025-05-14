from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect

from .forms import TodoForm
from .models import Todo


class TaskListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "task_list.html"

    def get_queryset(self):
        search = self.request.GET.get("search")
        ordering = self.request.GET.get("ordering")

        task_list = Todo.objects.filter(user=self.request.user)

        if search:
            task_list = task_list.filter(task__icontains=search)

        if ordering:
            ALLOWED_ORDERING_FIELDS = [
                "created_at",
                "-created_at",
                "due_date",
                "-due_date",
            ]
            if ordering in ALLOWED_ORDERING_FIELDS:
                task_list = task_list.order_by(ordering)

        return task_list


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "task_create.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "task_update.html"
    success_url = reverse_lazy("task_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


@login_required
def toggle_task_status(request, pk):
    task = get_object_or_404(Todo, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


@login_required
def completed_tasks_delete(request):
    tasks = Todo.objects.filter(user=request.user, completed=True)
    tasks.delete()
    return redirect("task_list")

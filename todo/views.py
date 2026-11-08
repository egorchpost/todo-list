from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.views import View
from django.views import generic

from todo.forms import TagForm, TaskForm
from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


class TaskToggleView(View):

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save(update_fields=["is_done"])

        next_url = request.POST.get("next") or request.META.get("HTTP_REFERER")
        if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}
        ):
            return redirect(next_url)
        return redirect("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")

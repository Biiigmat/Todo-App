from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageViews (TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.user_name if self.request.user.is_authenticated else None
        return context


class TaskCreateViews (CreateView, LoginRequiredMixin):
    model = Task
    template_name = 'task_create.html'
    form_class = TaskForm
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskListViews (ListView, LoginRequiredMixin):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetailViews (DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     return get_object_or_404(Task, pk=pk)


class TaskUpdateViews (UpdateView):
    model = Task
    template_name = 'task_update.html'
    context_object_name = 'task'
    form_class = TaskForm
    success_url = '/tasks/'


class TaskDeleteViews (DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = '/tasks/'
    success_message = 'The Task has been successfully deleted :)'
    context_object_name = 'task'


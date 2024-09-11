from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Task, TaskCategory


def index(request):
    latest_tasks_list = Task.objects.order_by('-id')
    context = {
        'latest_tasks_list': latest_tasks_list
    }

    return render(request, 'tasks/index.html', context)


def create(request):

    if request.method == 'POST':

        description = request.POST.get('description')
        title = request.POST.get('title')

        if title and description:
            task = Task(description=description, title=title)
            task.save()
            return HttpResponseRedirect(reverse('tasks:detail', args=(task.id,)))

        if not description or not title:
            messages.error(request, "Description and Title cannot be empty.")
            return render(request, 'tasks/create.html')

    return render(request, 'tasks/create.html')


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/detail.html", {'task': task})


def update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    try:
        description = request.POST.get('description')
        if description:
            task.description = description

        done = request.POST.get('done')
        task.done = bool(done)

    except KeyError:
        return render(request, 'tasks/detail.html', {'task': task, "error_message": "You didn't click the checkbox."})
    else:
        task.save()
        return HttpResponseRedirect(reverse('tasks:detail', args=(task.id,)))


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    messages.info(request, "item removed !!!")
    return HttpResponseRedirect(reverse('tasks:index'))


def filter_by_category(request, category_id):
    category = get_object_or_404(TaskCategory, pk=category_id)

    tasks = Task.objects.filter(category=category)

    context = {
        'latest_tasks_list': tasks
    }

    return render(request, "tasks/index.html", context)


def get_categories(request):
    categories = TaskCategory.objects.all()
    context = {
        'categories': categories
    }

    return render(request, "categories/index.html", context)



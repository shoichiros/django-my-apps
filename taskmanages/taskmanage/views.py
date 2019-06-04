from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
from .models import TaskCreate


def task_list(request):
    my_task = TaskCreate.objects.values()
    return render(request, 'taskmanage/top_page.html', {'my_task': my_task})


def task_create(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/')
        else:
            form = PostForm()
    return render(request, 'taskmanage/create_task.html', {'form': form})

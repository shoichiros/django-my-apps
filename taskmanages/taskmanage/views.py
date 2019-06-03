from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm


def task_list(request):
    return render(request, 'taskmanage/top_page.html')


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

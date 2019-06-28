from django.shortcuts import render
from .models import Test


def tests(request):
    # filter()
    data = Test.objects.values().filter(username='myuser')
    return render(request, 'index.html', {'data': data})

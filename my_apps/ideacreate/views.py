import csv
from django.shortcuts import render, HttpResponse
from .models import FirstWord, SecondWord, ThirdWord


def home(request):
    # Toppage
    return render(request, 'ideacreate/home.html')


def word_view(request):
    # Mainpage Wordcreateview
    first_list = FirstWord.objects.all()
    second_list = SecondWord.objects.all()
    third_list = ThirdWord.objects.all()
    context = {
        'first_list': first_list,
        'second_list': second_list,
        'third_list': third_list,
    }
    return render(request, 'ideacreate/word_view.html', context)


def upload(request):
    # CSV Upload
    # During creation
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefileaname.csv"'

    writer = csv.writer(response)
    writer.writerow([])
    return render(request, 'ideacreate/upload_csv.html')

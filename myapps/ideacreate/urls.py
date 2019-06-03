from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wordview/', views.word_view, name='wordview'),
    path('upload/', views.upload, name='upload'),
]

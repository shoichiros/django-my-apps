from django.urls import path
from accounts import views


urlpatterns = [
    path('', views.DefaultHomePageView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('privacy-policy/', views.PrivecyPolicyView.as_view(), name='privacy_policy'),
]

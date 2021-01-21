from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic, View
from django.urls import reverse, reverse_lazy

from accounts.forms import LoginForm
from accounts.admin import UserCreationForm


class DefaultHomePageView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'index.html')


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
            request,
            username=username,
            password=password,
            )

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'UsernameまたはPasswordが違います')
                return redirect('login')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return render(request, 'accounts/logout.html')


class PrivecyPolicyView(View):

    def get(self, request):
        return render(request, 'accounts/privacy_policy.html')

from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models, forms

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы вошли как {username}.")
                return redirect(reverse_lazy('user:personal-account-list'))
            else:
                messages.error(request, "Неправильное имя пользователя или пароль.")
        else:
            messages.error(request, "Неправильное имя пользователя или пароль.")
            messages.error(request, "Пройдите регистрацию или продолжите как не зарегистрированный пользователь.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "user_app/login_entrance.html",
                  context={"form":form})



def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из системы.")
    return redirect((reverse_lazy('user:home-page-list')))




def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse_lazy('user:personal-account-list'))
    else:
        form = UserCreationForm()
    return render(request, 'user_app/registration.html', {'form': form})



class PersonalAccountList(generic.ListView):
    model = models.PersonalAccount


class HomePageList(generic.ListView):
    model = models.HomePage


class MyLoginView(auth_views.LoginView):
    template_name = "user_app/login.html"
   


class JobList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'user_app.view_job' 
    login_url = reverse_lazy('user:login')
    model = models.Job
    template_name = 'user_app/job_list.html'
    context_object_name = 'jobs'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'name') 
        return queryset.order_by(ordering) 
    

class JobCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):  
    permission_required = 'user_app.add_job' 
    login_url = reverse_lazy('user:login')
    model = models.Job
    fields = ['name',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание должности:"
        return context


class JobUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView): 
    permission_required = 'user_app.change_job'
    login_url = reverse_lazy('user:login')
    model = models.Job
    fields = ['name', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать данные:"
        return context


class JobDelete(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    permission_required = 'user_app.delete_job'
    login_url = reverse_lazy('user:login')
    model = models.Job
    success_url = reverse_lazy('user:job-list')



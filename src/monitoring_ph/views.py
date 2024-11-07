from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from . models import Organization
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .forms import Monitoring_phForm
from PIL import Image
import os


class Monitoring_phList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = 'monitoring_ph.view_monitoring_ph' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ph
    template_name = 'monitoring_ph/monitoring_ph_list.html'
    context_object_name = 'monitoring_ph'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class Monitoring_phDetail(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = 'monitoring_ph.view_monitoring_ph' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ph


class Monitoring_phCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):  
    permission_required = 'monitoring_ph.add_monitoring_ph' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ph
    
    def get(self, request):
        form = Monitoring_phForm()
        return render(request, 'monitoring_ph/monitoring_ph_form.html', {'form': form})

    def post(self, request):
        form = Monitoring_phForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем последнюю просмотренную организацию из сессии
            last_organization_id = request.session.get('last_organization_id')
            if last_organization_id:
                # Если организация найдена, устанавливаем её в форму
                form.instance.organization = Organization.objects.get(id=last_organization_id)
   
            # Сохраняем объект мониторинга
            monitoring_ph = form.save()
            return redirect('consultants:organization-list')  # Перенаправляем на список мониторингов
        return render(request, 'monitoring_ph/monitoring_ph_form.html', {'form': form})   



class Monitoring_phUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):   
    permission_required = 'monitoring_ph.change_monitoring_ph' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ph
    fields = ['date', 'group', 'animal_1', 'animal_2', 'animal_3', 'animal_4',
              'animal_5', 'animal_6', 'animal_7', 'animal_8', 'animal_9', 'animal_10',
              'ph_1', 'ph_2', 'ph_3', 'ph_4',
              'ph_5', 'ph_6', 'ph_7', 'ph_8', 'ph_9', 'ph_10',
              'recommendations', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "(изменение)"
        return context


from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from . models import Organization
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .forms import Monitoring_ketForm
from PIL import Image
import os


class Monitoring_ketList(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView): 
    permission_required = 'monitoring_ket.view_monitoring_ket' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ket
    template_name = 'monitoring_ket/monitoring_ket_list.html'
    context_object_name = 'monitoring_ket'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class Monitoring_ketDetail(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    permission_required = 'monitoring_ket.view_monitoring_ket' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ket


class Monitoring_ketCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):  
    permission_required = 'monitoring_ket.add_monitoring_ket' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ket
    
    def get(self, request):
        form = Monitoring_ketForm()
        return render(request, 'monitoring_ket/monitoring_ket_form.html', {'form': form})

    def post(self, request):
        form = Monitoring_ketForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем последнюю просмотренную организацию из сессии
            last_organization_id = request.session.get('last_organization_id')
            if last_organization_id:
                # Если организация найдена, устанавливаем её в форму
                form.instance.organization = Organization.objects.get(id=last_organization_id)
   
            # Сохраняем объект мониторинга
            monitoring_ket = form.save()
            return redirect('consultants:organization-list')  # Перенаправляем на список мониторингов
        return render(request, 'monitoring_ket/monitoring_ket_form.html', {'form': form})   



class Monitoring_ketUpdate(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView): 
    permission_required = 'monitoring_ket.change_monitoring_ket' 
    login_url = reverse_lazy('user:login')
    model = models.Monitoring_ket
    fields = ['date', 'group',
                  'animal_1', 'keton_1',
                  'animal_2', 'keton_2',
                  'animal_3', 'keton_3',
                  'animal_4', 'keton_4',
                  'animal_5', 'keton_5',
                  'animal_6', 'keton_6',
                  'animal_7', 'keton_7',
                  'animal_8', 'keton_8',
                  'animal_9', 'keton_9',
                  'animal_10', 'keton_10',
                  'animal_11', 'keton_11',
                  'animal_12', 'keton_12',
                  'animal_13', 'keton_13',
                  'animal_14', 'keton_14',
                  'animal_15', 'keton_15',
                  'recommendations', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "(изменение)"
        return context



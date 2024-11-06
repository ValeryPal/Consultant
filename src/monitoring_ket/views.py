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


class Monitoring_ketList(generic.ListView): # PermissionRequiredMixin, 
    model = models.Monitoring_ket
    template_name = 'monitoring_ket/monitoring_ket_list.html'
    context_object_name = 'monitoring_ket'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class Monitoring_ketDetail(generic.DetailView):
    model = models.Monitoring_ket


class Monitoring_ketCreate(generic.CreateView): #LoginRequiredMixin, PermissionRequiredMixin, 
    # permission_required = 'book_shop_app.add_author' 
    # login_url = reverse_lazy('user:login')
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



class Monitoring_ketUpdate(generic.UpdateView):  #LoginRequiredMixin, PermissionRequiredMixin, 
    #permission_required = 'book_shop_app.change_author'
    #login_url = reverse_lazy('user:login')
    model = models.Monitoring_ket
    fields = ['date', 'group', 'animal_1', 'animal_2', 'animal_3', 'animal_4',
              'animal_5', 'animal_6', 'animal_7', 'animal_8', 'animal_9', 'animal_10',
              'animal_11', 'animal_12', 'animal_13', 'animal_14', 'animal_15',
              'keton_1', 'keton_2', 'keton_3', 'keton_4',
              'keton_5', 'keton_6', 'keton_7', 'keton_8', 'keton_9', 'keton_10',
              'keton_11', 'keton_12', 'keton_13', 'keton_14', 'keton_15',
              'recommendations', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "(изменение)"
        return context



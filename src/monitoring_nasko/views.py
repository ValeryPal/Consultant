from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from . models import Organization
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .forms import Monitoring_naskoForm
from PIL import Image
import os


class Monitoring_naskoList(generic.ListView): # PermissionRequiredMixin, 
    model = models.Monitoring_nasko
    template_name = 'monitoring_nasko/monitorings_nasko_list.html'
    context_object_name = 'monitoring_naskos'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class Monitoring_naskoDetail(generic.DetailView):
    model = models.Monitoring_nasko


class Monitoring_naskoCreate(generic.CreateView): #LoginRequiredMixin, PermissionRequiredMixin, 
    # permission_required = 'book_shop_app.add_author' 
    # login_url = reverse_lazy('user:login')
    model = models.Monitoring_nasko
    
    def get(self, request):
        form = Monitoring_naskoForm()
        return render(request, 'monitoring_nasko/monitoring_nasko_form.html', {'form': form})

    def post(self, request):
        form = Monitoring_naskoForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем последнюю просмотренную организацию из сессии
            last_organization_id = request.session.get('last_organization_id')
            if last_organization_id:
                # Если организация найдена, устанавливаем её в форму
                form.instance.organization = Organization.objects.get(id=last_organization_id)
   
            # Сохраняем объект мониторинга
            monitoring_nasko = form.save()
            return redirect('consultants:organization-list')  # Перенаправляем на список мониторингов
        return render(request, 'monitoring_nasko/monitoring_nasko_form.html', {'form': form})   



class Monitoring_naskoUpdate(generic.UpdateView):  #LoginRequiredMixin, PermissionRequiredMixin, 
    #permission_required = 'book_shop_app.change_author'
    #login_url = reverse_lazy('user:login')
    model = models.Monitoring_nasko
    fields = ['date', 'group', 'feces_1', 'feces_2', 'feces_3',
              'foto_1', 'foto_2', 'foto_3',
              'feces_mixture', 'recommendations', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "(изменение)"
        return context


from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from . models import Organization
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .forms import MonitoringForm
from PIL import Image
import os


class MonitoringFeedList(generic.ListView): # PermissionRequiredMixin, 
    model = models.MonitoringFeed
    template_name = 'monitoring/monitorings_list.html'
    context_object_name = 'monitorings'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class MonitoringFeedDetail(generic.DetailView):
    model = models.MonitoringFeed


class MonitoringFeedCreate(generic.CreateView): #LoginRequiredMixin, PermissionRequiredMixin, 
    # permission_required = 'book_shop_app.add_author' 
    # login_url = reverse_lazy('user:login')
    model = models.MonitoringFeed
    
    def get(self, request):
        form = MonitoringForm()
        return render(request, 'monitoring/monitoringfeed_form.html', {'form': form})

    def post(self, request):
        form = MonitoringForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем последнюю просмотренную организацию из сессии
            last_organization_id = request.session.get('last_organization_id')
            if last_organization_id:
                # Если организация найдена, устанавливаем её в форму
                form.instance.organization = Organization.objects.get(id=last_organization_id)
   
            # Сохраняем объект мониторинга
            monitoringfeed = form.save()
            return redirect('consultants:organization-list')  # Перенаправляем на список мониторингов
        return render(request, 'monitoring/monitoringfeed_form.html', {'form': form})   



class MonitoringFeedUpdate(generic.UpdateView):  #LoginRequiredMixin, PermissionRequiredMixin, 
    #permission_required = 'book_shop_app.change_author'
    #login_url = reverse_lazy('user:login')
    model = models.MonitoringFeed
    fields = ['group', 'feed_1', 'feed_2', 'feed_3', 'feed_4',
              'foto_1', 'foto_2', 'foto_3', 'foto_4',
              'feed_mixture', 'recommendations', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Изменение мониторинга кормосмеси:"
        return context

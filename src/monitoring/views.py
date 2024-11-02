from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from . models import Organization
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator



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
    fields = ['organization', 'date',
              'foto_1', 'foto_2', 'foto_3', 'foto_4',
              'feed_mixture', 'job', 'user_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Создание мониторинга кормосмеси:"
        return context
    

class MonitoringFeedUpdate(generic.UpdateView):  #LoginRequiredMixin, PermissionRequiredMixin, 
    #permission_required = 'book_shop_app.change_author'
    #login_url = reverse_lazy('user:login')
    model = models.MonitoringFeed
    fields = ['organization', 'date',
              'foto_1', 'foto_2', 'foto_3', 'foto_4',
              'feed_mixture', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Изменение мониторинга кормосмеси:"
        return context

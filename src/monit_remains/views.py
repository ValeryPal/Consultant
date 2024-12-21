from django.shortcuts import render
from . import models
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from . models import Organization
from .forms import RemainForm
from django.shortcuts import render, get_object_or_404, redirect


class RemainList(LoginRequiredMixin, generic.ListView): 
    login_url = reverse_lazy('user:login')
    model = models.Remain
    template_name = 'monit_remains/monit_remains_list.html'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class RemainCreate(LoginRequiredMixin, generic.CreateView):  
    login_url = reverse_lazy('user:login')
    model = models.Remain
    
    def get(self, request):
        form = RemainForm()
        return render(request, 'monit_remains/monit_remains_form.html', {'form': form})

    def post(self, request):
        form = RemainForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем последнюю просмотренную организацию из сессии
            last_organization_id = request.session.get('last_organization_id')
            if last_organization_id:
                # Если организация найдена, устанавливаем её в форму
                form.instance.organization = Organization.objects.get(id=last_organization_id)
   
            # Сохраняем объект мониторинга
            monitoring_ph = form.save()
            return redirect('consultants:organization-list')  # Перенаправляем на список мониторингов
        return render(request, 'monit_remains/monit_remains_form.html', {'form': form})  


class RemainDetail(LoginRequiredMixin, generic.DetailView): 
    login_url = reverse_lazy('user:login')
    model = models.Remain


class RemainUpdate(LoginRequiredMixin, generic.UpdateView):    
    login_url = reverse_lazy('user:login')
    model = models.Remain
    template_name = 'monit_remains/monit_remains_form.html'
    fields = ['date', 'user_name', 'products']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "(изменение)"
        return context
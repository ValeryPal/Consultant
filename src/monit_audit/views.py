from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from . models import Organization
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .forms import MonitAuditMilkForm



class MonitAuditMilkList(LoginRequiredMixin,  generic.ListView): #PermissionRequiredMixin,
    #permission_required = 'monit_audit.view_monit_audit_milk'
    login_url = reverse_lazy('user:login') 
    model = models.MonitAuditMilk
    template_name = 'monit_audit/audit_list.html'
    context_object_name = 'monit_audits'
    paginate_by = 20
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class MonitAuditMilkDetail(LoginRequiredMixin, generic.DetailView): #PermissionRequiredMixin,
    #permission_required = 'monit_audit_milk.view_monit_audit_milk' 
    login_url = reverse_lazy('user:login') 
    model = models.MonitAuditMilk
    template_name = 'monit_audit/monitauditmilk_detail.html'

class MonitAuditMilkCreate(LoginRequiredMixin, generic.CreateView): #PermissionRequiredMixin,
    #permission_required = 'monit_audit.add_monit_audit_milk' 
    login_url = reverse_lazy('user:login')
    model = models.MonitAuditMilk
    
    def get(self, request):
        form = MonitAuditMilkForm()
        return render(request, 'monit_audit/audit_form.html', {'form': form})

    def post(self, request):
        form = MonitAuditMilkForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем последнюю просмотренную организацию из сессии
            last_organization_id = request.session.get('last_organization_id')
            if last_organization_id:
                # Если организация найдена, устанавливаем её в форму
                form.instance.organization = Organization.objects.get(id=last_organization_id)
   
            # Сохраняем объект мониторинга
            monitauditmilk = form.save()
            return redirect('consultants:organization-list')  # Перенаправляем на список мониторингов
        return render(request, 'monit_audit/audit_form.html', {'form': form})   



class MonitAuditMilkUpdate(LoginRequiredMixin, generic.UpdateView):   #PermissionRequiredMixin, 
    #permission_required = 'monit_audit.change_monit_audit'
    login_url = reverse_lazy('user:login')
    model = models.MonitAuditMilk
    template_name = 'monit_audit/audit_form.html'
    fields = ['date', 'content', 'livestock', 'dairy_cattle', 'days_lactation',
                  'milk', 'milk_cow', 'milk_sales', 'milk_fat', 'milk_protein', 'milk_somatics',
                   'number_milkings', 'weight_cow', 'number_calvings', 'calf_weight',
                    'groups', 'diet_composition', 'diet_composition_feed', 'notes_diet',
                     'notes_animall', 'withdrawal', 'notes', 'offers', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "(изменение)"
        return context


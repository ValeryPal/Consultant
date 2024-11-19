from django.shortcuts import render
from . import models
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from . models import Organization
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from .forms import MonitAuditCalvesForm



class MonitAuditCalvesList(LoginRequiredMixin,  generic.ListView): #PermissionRequiredMixin,
    #permission_required = 'monit_audit.view_monit_audit_milk'
    login_url = reverse_lazy('user:login') 
    model = models.MonitAuditCalves
    template_name = 'monit_calves/calves_list.html'
    context_object_name = 'monit_calves'
    paginate_by = 20
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering', 'date') 
        return queryset.order_by(ordering) 


class MonitAuditCalvesDetail(LoginRequiredMixin, generic.DetailView): #PermissionRequiredMixin,
    #permission_required = 'monit_audit_milk.view_monit_audit_milk' 
    login_url = reverse_lazy('user:login') 
    model = models.MonitAuditCalves
    template_name = 'monit_calves/monitauditcalves_detail.html'

class MonitAuditCalvesCreate(LoginRequiredMixin, generic.CreateView): #PermissionRequiredMixin,
    #permission_required = 'monit_audit.add_monit_audit_milk' 
    login_url = reverse_lazy('user:login')
    model = models.MonitAuditCalves
    
    def get(self, request):
        form = MonitAuditCalvesForm()
        return render(request, 'monit_calves/calves_form.html', {'form': form})

    def post(self, request):
        form = MonitAuditCalvesForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем последнюю просмотренную организацию из сессии
            last_organization_id = request.session.get('last_organization_id')
            if last_organization_id:
                # Если организация найдена, устанавливаем её в форму
                form.instance.organization = Organization.objects.get(id=last_organization_id)
   
            # Сохраняем объект мониторинга
            monitauditcalves = form.save()
            return redirect('consultants:organization-list')  # Перенаправляем на список мониторингов
        return render(request, 'monit_calves/calves_form.html', {'form': form})   



class MonitAuditCalvesUpdate(LoginRequiredMixin, generic.UpdateView):   #PermissionRequiredMixin, 
    #permission_required = 'monit_audit.change_monit_audit'
    login_url = reverse_lazy('user:login')
    model = models.MonitAuditCalves
    template_name = 'monit_calves/calves_form.html'
    fields = ['date', 'content', 'livestock_calves', 'weight_calves', 'number_boxes',
                  'number_calf', 'number_milk', 'calf_weight', 'number_calvings',
                    'groups', 'offers_1', 'diet_composition', 'notes_diet', 'diet_composition_feed', 'offers_2',
                     'notes_animall', 'offers_3', 'withdrawal', 'offers_4', 'notes', 'offers', 'job', 'user_name']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "(изменение)"
        return context



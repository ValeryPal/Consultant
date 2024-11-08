from django.urls import reverse_lazy
from django.views import generic
from .models import Organization, Consultant
from .forms import OrganizationForm
from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Поиск по названию организации
def search(request):
    query = request.GET.get('q')
    organization = models.Organization.objects
    organizations = []
    if query:
        organizations = Organization.objects.filter(name__icontains=query)  # Поиск по названию организации
    return render(request, 'consultants/search_results.html', {'organizations': organizations, 'query': organization})

# Поиск по названию фермы
def search_farm(request):
    query = request.GET.get('q')
    organization = models.Organization.objects
    organizations = []
    if query:
        organizations = Organization.objects.filter(farm__icontains=query)  # Поиск по названию фермы
    return render(request, 'consultants/search_results_farm.html', {'organizations': organizations, 'query': organization})


class OrganizationListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    """Список организаций, доступных текущему консультанту."""
    permission_required = 'consultants.view_organization' 
    login_url = reverse_lazy('user:login')
    model = Organization
    template_name = 'consultants/organization_list.html'

    def get_queryset(self):
        # Ограничиваем queryset так, чтобы возвращались только организации текущего консультанта
        consultant = self.request.user.consultant
        return Organization.objects.filter(consultant=consultant)

class OrganizationCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    """Создание новой организации."""
    permission_required = 'consultants.add_organization' 
    login_url = reverse_lazy('user:login')
    model = Organization
    form_class = OrganizationForm
    template_name = 'consultants/organization_form.html'
    success_url = reverse_lazy('consultants:organization-list')

    def form_valid(self, form):
        # Устанавливаем консультанта пользователя как владельца создаваемой организации
        form.instance.consultant = self.request.user.consultant
        return super().form_valid(form)

class OrganizationDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    """Детали организации."""
    permission_required = 'consultants.view_organization' 
    login_url = reverse_lazy('user:login')
    model = Organization
    template_name = 'consultants/organization_detail.html'

    def get(self, request, pk):
        organization = Organization.objects.get(pk=pk)
        # Сохраняем ID организации в сессию
        request.session['last_organization_id'] = organization.id
        return render(request, 'consultants/organization_detail.html', {'organization': organization})

    def get_queryset(self):
        # Ограничиваем queryset, чтобы только наш консультант мог видеть детали своей организации
        consultant = self.request.user.consultant
        return Organization.objects.filter(consultant=consultant)

    
class OrganizationUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    """Обновление существующей организации."""
    permission_required = 'consultants.change_organization' 
    login_url = reverse_lazy('user:login')
    model = Organization
    form_class = OrganizationForm
    template_name = 'consultants/organization_form.html'
    success_url = reverse_lazy('consultants:organization-list')

    def get_queryset(self):
        # Ограничиваем queryset для редактирования только для организаций текущего консультанта
        consultant = self.request.user.consultant
        return Organization.objects.filter(consultant=consultant)

class OrganizationDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    """Удаление организации."""
    permission_required = 'consultants.delete_organization' 
    login_url = reverse_lazy('user:login')
    model = Organization
    template_name = 'consultants/organization_confirm_delete.html'
    success_url = reverse_lazy('consultants:organization-list')
    
    def get_queryset(self):
        # Ограничиваем queryset для удаления только для организаций текущего консультанта
        consultant = self.request.user.consultant
        return Organization.objects.filter(consultant=consultant)


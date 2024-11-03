from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Organization, Consultant
from .forms import OrganizationForm
from django.shortcuts import render, redirect

class OrganizationListView(LoginRequiredMixin, generic.ListView):
    """Список организаций, доступных текущему консультанту."""
    model = Organization
    template_name = 'consultants/organization_list.html'

    def get_queryset(self):
        # Ограничиваем queryset так, чтобы возвращались только организации текущего консультанта
        consultant = self.request.user.consultant
        return Organization.objects.filter(consultant=consultant)

class OrganizationCreateView(LoginRequiredMixin, generic.CreateView):
    """Создание новой организации."""
    model = Organization
    form_class = OrganizationForm
    template_name = 'consultants/organization_form.html'
    success_url = reverse_lazy('consultants:organization-list')

    def form_valid(self, form):
        # Устанавливаем консультанта пользователя как владельца создаваемой организации
        form.instance.consultant = self.request.user.consultant
        return super().form_valid(form)

class OrganizationDetailView(LoginRequiredMixin, generic.DetailView):
    """Детали организации."""
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

    
    

class OrganizationUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Обновление существующей организации."""
    model = Organization
    form_class = OrganizationForm
    template_name = 'consultants/organization_form.html'
    success_url = reverse_lazy('consultants:organization-list')

    def get_queryset(self):
        # Ограничиваем queryset для редактирования только для организаций текущего консультанта
        consultant = self.request.user.consultant
        return Organization.objects.filter(consultant=consultant)

class OrganizationDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Удаление организации."""
    model = Organization
    template_name = 'consultants/organization_confirm_delete.html'
    success_url = reverse_lazy('consultants:organization-list')

    def get_queryset(self):
        # Ограничиваем queryset для удаления только для организаций текущего консультанта
        consultant = self.request.user.consultant
        return Organization.objects.filter(consultant=consultant)



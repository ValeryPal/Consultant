from django.urls import path
from . import views


app_name = "consultants"

urlpatterns = [
    path('organization-list/', views.OrganizationListView.as_view(), name='organization-list'),
    path('organization-create/', views.OrganizationCreateView.as_view(), name='organization-create'),
    path('organization-detail/<int:pk>/', views.OrganizationDetailView.as_view(), name='organization-detail'),
    path('organization-update/<int:pk>/', views.OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization-delete/<int:pk>/', views.OrganizationDeleteView.as_view(), name='organization-delete'),
    path('search/', views.search, name='search'),
]

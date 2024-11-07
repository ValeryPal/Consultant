from django.urls import path
from . import views


app_name = "consultants"

urlpatterns = [
    path('organization-list/', views.OrganizationListView.as_view(), name='organization-list'),
    path('5/65/23/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/69/58/56/7/9/11/10/', views.OrganizationCreateView.as_view(), name='organization-create'),
    path('5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/<int:pk>/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/', views.OrganizationDetailView.as_view(), name='organization-detail'),
    path('5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/<int:pk>/', views.OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization-delete/<int:pk>/', views.OrganizationDeleteView.as_view(), name='organization-delete'),
    path('search/', views.search, name='search'),
]

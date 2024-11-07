
from django.urls import path
from . import views

app_name = "monitoring_nasko"

urlpatterns = [  
    path("5/65/23/4/9/36/65/18/3/9/498/6/2/9/", views.Monitoring_naskoList.as_view(), name="monitoring-nasko-list"),
    path('5/65/23/4/9/36/12/9/78/21/69/58/<int:pk>/56/7/9/11/10/', views.Monitoring_naskoDetail.as_view(), name="monitoring-nasko-detail"),
    path('5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/', views.Monitoring_naskoCreate.as_view(), name="monitoring-nasko-create"),
    path('5/65/23/4/9/36/12/15/56/7/9/11/10/<int:pk>/', views.Monitoring_naskoUpdate.as_view(), name="monitoring-nasko-update"),
]

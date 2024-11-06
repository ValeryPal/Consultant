
from django.urls import path
from . import views

app_name = "monitoring_ket"

urlpatterns = [  
    path("5/65/23/4/9/36/65/18/3/9/498/6/2/9/", views.Monitoring_ketList.as_view(), name="monitoring-ket-list"),
    path('5/65/23/4/9/36/12/9/78/21/69/58/<int:pk>/56/7/9/11/10/', views.Monitoring_ketDetail.as_view(), name="monitoring-ket-detail"),
    path('5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/', views.Monitoring_ketCreate.as_view(), name="monitoring-ket-create"),
    path('5/65/23/4/9/36/12/15/56/7/9/11/10/<int:pk>/', views.Monitoring_ketUpdate.as_view(), name="monitoring-ket-update"),
]

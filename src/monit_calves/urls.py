
from django.urls import path
from . import views

app_name = "monit_calves"

urlpatterns = [  
    path("65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/", views.MonitAuditCalvesList.as_view(), name="calves-list"),
    path('5/65/23/4/96/36/12/9/78/21/169/58/56/7/65/1223/4/9/36/12/9/78/21/1238/58/9/123/10/<int:pk>/', views.MonitAuditCalvesDetail.as_view(), name="calves-detail"),
    path('5/65/23/4/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/58/56/7/9/11/10/', views.MonitAuditCalvesCreate.as_view(), name="calves-create"),
    path('65/23/4/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/58/56/7/<int:pk>/', views.MonitAuditCalvesUpdate.as_view(), name="calves-update"),
]


from django.urls import path
from . import views

app_name = "monit_audit"

urlpatterns = [  
    path("65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/", views.MonitAuditMilkList.as_view(), name="audit-list"),
    path('5/65/23/4/96/36/12/9/78/21/169/58/56/7/65/1223/4/9/36/12/9/78/21/1238/58/9/123/10/<int:pk>/', views.MonitAuditMilkDetail.as_view(), name="audit-detail"),
    path('5/65/23/4/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/58/56/7/9/11/10/', views.MonitAuditMilkCreate.as_view(), name="audit-create"),
    path('65/23/4/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/58/56/7/<int:pk>/', views.MonitAuditMilkUpdate.as_view(), name="audit-update"),
]


from django.urls import path
from . import views

app_name = "monit_remains"

urlpatterns = [  
    path("monit_remains_list", views.RemainList.as_view(), name="monit-remains-list"),
    path('monit_remains_create', views.RemainCreate.as_view(), name='monit-remains-create'),
    path('5/65/23/4/9/36/12/9/78/21/69/58/<int:pk>/56/7/9/11/10/', views.RemainDetail.as_view(), name="monit-remains-detail"),
    path('5/65/23/4/9/36/12/15/56/7/9/11/10/<int:pk>/', views.RemainUpdate.as_view(), name="monit-remains-update"),
]

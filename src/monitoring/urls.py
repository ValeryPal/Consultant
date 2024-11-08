
from django.urls import path
from . import views

app_name = "monitoring"

urlpatterns = [  
    path("65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/", views.MonitoringFeedList.as_view(), name="monitoringfeeds-list"),
    path('5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/<int:pk>/', views.MonitoringFeedDetail.as_view(), name="monitoringfeeds-detail"),
    path('5/65/23/4/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/58/56/7/9/11/10/', views.MonitoringFeedCreate.as_view(), name="monitoringfeeds-create"),
    path('65/23/4/5/65/23/4/9/36/12/9/78/21/69/58/56/7/9/11/10/58/56/7/<int:pk>/', views.MonitoringFeedUpdate.as_view(), name="monitoringfeeds-update"),
]


from django.urls import path
from . import views

app_name = "monitoring"

urlpatterns = [  
    path("monitoringfeeds-list/", views.MonitoringFeedList.as_view(), name="monitoringfeeds-list"),
    path('monitoringfeeds-detail/<int:pk>/', views.MonitoringFeedDetail.as_view(), name="monitoringfeeds-detail"),
    path('monitoringfeeds-create/', views.MonitoringFeedCreate.as_view(), name="monitoringfeeds-create"),
    path('monitoringfeeds-update/<int:pk>/', views.MonitoringFeedUpdate.as_view(), name="monitoringfeeds-update"),
]

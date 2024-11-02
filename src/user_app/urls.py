
from django.urls import path, include
from . import views
from . views import registration, login_view, logout_view

app_name = "user"

urlpatterns = [  
    path("home-page-list/", views.HomePageList.as_view(), name="home-page-list"),
    path('registration/', registration, name="registration"),
    path("personal-account-list/", views.PersonalAccountList.as_view(), name="personal-account-list"),
    path('login/', views.MyLoginView.as_view(), name="login"), 
    path("login_entrance/", login_view, name="login_entrance"),
    path("logout/", logout_view, name="logout"),
    path("job-list/", views.JobList.as_view(), name="job-list"),
    path('job-create/', views.JobCreate.as_view(), name="job-create"),
    path('job-update/<int:pk>/', views.JobUpdate.as_view(), name="job-update"),
    path('job-delete/<int:pk>/', views.JobDelete.as_view(), name="job-delete"),

    
    
    # path('profile-detail/', views.CustomerDetail.as_view(), name="profile-detail"), 
    # path('profile-create/', views.CustomerCreate.as_view(), name="profile-create"),
    # path('profile-update/<int:pk>/', views.CustomerUpdate.as_view(), name="profile-update"),
     
    
]
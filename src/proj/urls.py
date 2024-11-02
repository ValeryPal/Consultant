from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_app.urls', namespace='user')),
    path('consultants/', include('consultants.urls', namespace='consultants')),
    path('monitoring/', include('monitoring.urls', namespace='monitoring')),
    # path('depatments/', include('depatments.urls', namespace='depatments')),
    # path('audits/', include('audits.urls', namespace='audits')),
    
    #          
]

# не для хостинга
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_app.urls', namespace='user')),
    path('consultants/', include('consultants.urls', namespace='consultants')),
    path('monitoring/', include('monitoring.urls', namespace='monitoring')),
    path('monitoring_ph/', include('monitoring_ph.urls', namespace='monitoring_ph')),
    path('monitoring_ket/', include('monitoring_ket.urls', namespace='monitoring_ket')),
    path('monitoring_nasko/', include('monitoring_nasko.urls', namespace='monitoring_nasko')),
    path('monit_audit/', include('monit_audit.urls', namespace='monit_audit')),
    path('monit_calves/', include('monit_calves.urls', namespace='monit_calves')),
]

# не для хостинга
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


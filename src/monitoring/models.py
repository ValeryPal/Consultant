from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from consultants.models import Organization
from user_app.models import Job
from django.contrib.auth import get_user_model # вместо user


User = get_user_model()

# Приложение 1 (мониторинг кормосмеси)
class MonitoringFeed(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='monitoringfeeds',)
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, null=True)   
    
    foto_1 = models.ImageField(verbose_name='Фото верхнего сита 19 мм', upload_to='foto_monitoring/%Y/%m/%d', )      # фото верхнего сита 19 мм
    foto_2 = models.ImageField(verbose_name='Фото среднего сита 8 мм', upload_to='foto_monitoring/%Y/%m/%d', )     # фото среднего сита 8 мм
    foto_3 = models.ImageField(verbose_name='Фото нижнего сита 4 мм', upload_to='foto_monitoring/%Y/%m/%d', )      # фото нижнего сита 4 мм
    foto_4 = models.ImageField(verbose_name='Фото поддона', upload_to='foto_monitoring/%Y/%m/%d',)      # фото поддона
    feed_mixture = models.TextField(verbose_name='Замечания по кормосмеси', max_length=4000, null=True)
    
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

    def __str__(self):
        return f' {self.organization}'

    def get_absolute_url(self):
       return reverse_lazy('monitoring:monitoringfeeds-detail', kwargs={"pk": self.pk})  






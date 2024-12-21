from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from consultants.models import Organization
from django.contrib.auth import get_user_model # вместо user
from user_app.models import Job

User = get_user_model()

#  (мониторинг остатков)
class Remain(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='remains',)
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, null=True)   
    
    products = models.TextField(verbose_name='Остатки продукции и количество',  null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

    def get_absolute_url(self):
       return reverse_lazy('monit_remains:monit-remains-detail', kwargs={"pk": self.pk}) 

    def __str__(self):
        return f'{self.date}  -  {self.products}'




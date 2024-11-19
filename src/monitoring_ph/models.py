from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from consultants.models import Organization
from user_app.models import Job
from django.contrib.auth import get_user_model # вместо user
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from PIL import Image as PILImage
import os
from io import BytesIO
from django.core.files.base import ContentFile


User = get_user_model()

#  (мониторинг ph мочи)
class Monitoring_ph(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='monitoring_phs',)
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, null=True)   
    ###
    group = models.CharField(verbose_name='Группа животных', max_length=100, null=True)
    ###
    animal_1 = models.IntegerField(verbose_name='Номер 1 животного', null=True, blank=True)
    animal_2 = models.IntegerField(verbose_name='Номер 2 животного', null=True, blank=True)
    animal_3 = models.IntegerField(verbose_name='Номер 3 животного', null=True, blank=True)
    animal_4 = models.IntegerField(verbose_name='Номер 4 животного', null=True, blank=True)
    animal_5 = models.IntegerField(verbose_name='Номер 5 животного', null=True, blank=True)
    animal_6 = models.IntegerField(verbose_name='Номер 6 животного', null=True, blank=True)
    animal_7 = models.IntegerField(verbose_name='Номер 7 животного', null=True, blank=True)
    animal_8 = models.IntegerField(verbose_name='Номер 8 животного', null=True, blank=True)
    animal_9 = models.IntegerField(verbose_name='Номер 9 животного', null=True, blank=True)
    animal_10 = models.IntegerField(verbose_name='Номер 10 животного', null=True, blank=True)
    ###
    ph_1 = models.FloatField(verbose_name='ph 1 животного', null=True, blank=True)
    ph_2 = models.FloatField(verbose_name='ph 2 животного', null=True, blank=True)
    ph_3 = models.FloatField(verbose_name='ph 3 животного', null=True, blank=True)
    ph_4 = models.FloatField(verbose_name='ph 4 животного', null=True, blank=True)
    ph_5 = models.FloatField(verbose_name='ph 5 животного', null=True, blank=True)
    ph_6 = models.FloatField(verbose_name='ph 6 животного', null=True, blank=True)
    ph_7 = models.FloatField(verbose_name='ph 7 животного', null=True, blank=True)
    ph_8 = models.FloatField(verbose_name='ph 8 животного', null=True, blank=True)
    ph_9 = models.FloatField(verbose_name='ph 9 животного', null=True, blank=True)
    ph_10 = models.FloatField(verbose_name='ph 10 животного', null=True, blank=True)
    ###
    recommendations = models.TextField(verbose_name='Рекомендации',  null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

    
    def get_absolute_url(self):
       return reverse_lazy('monitoring_ph:monitoring-ph-detail', kwargs={"pk": self.pk})  

    def __str__(self):
        return f'{self.date}  -  {self.organization}'



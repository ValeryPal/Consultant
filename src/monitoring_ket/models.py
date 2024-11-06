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

#  (мониторинг keton мочи)
class Monitoring_ket(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='monitoring_kets',)
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
    animal_11 = models.IntegerField(verbose_name='Номер 11 животного', null=True, blank=True)
    animal_12 = models.IntegerField(verbose_name='Номер 12 животного', null=True, blank=True)
    animal_13 = models.IntegerField(verbose_name='Номер 13 животного', null=True, blank=True)
    animal_14 = models.IntegerField(verbose_name='Номер 14 животного', null=True, blank=True)
    animal_15 = models.IntegerField(verbose_name='Номер 15 животного', null=True, blank=True)
    ###
    keton_1 = models.FloatField(verbose_name='Кетоны 1 животного', null=True, blank=True)
    keton_2 = models.FloatField(verbose_name='Кетоны 2 животного', null=True, blank=True)
    keton_3 = models.FloatField(verbose_name='Кетоны 3 животного', null=True, blank=True)
    keton_4 = models.FloatField(verbose_name='Кетоны 4 животного', null=True, blank=True)
    keton_5 = models.FloatField(verbose_name='Кетоны 5 животного', null=True, blank=True)
    keton_6 = models.FloatField(verbose_name='Кетоны 6 животного', null=True, blank=True)
    keton_7 = models.FloatField(verbose_name='Кетоны 7 животного', null=True, blank=True)
    keton_8 = models.FloatField(verbose_name='Кетоны 8 животного', null=True, blank=True)
    keton_9 = models.FloatField(verbose_name='Кетоны 9 животного', null=True, blank=True)
    keton_10 = models.FloatField(verbose_name='Кетоны 10 животного', null=True, blank=True)
    keton_11 = models.FloatField(verbose_name='Кетоны 11 животного', null=True, blank=True)
    keton_12 = models.FloatField(verbose_name='Кетоны 12 животного', null=True, blank=True)
    keton_13 = models.FloatField(verbose_name='Кетоны 13 животного', null=True, blank=True)
    keton_14 = models.FloatField(verbose_name='Кетоны 14 животного', null=True, blank=True)
    keton_15 = models.FloatField(verbose_name='Кетоны 15 животного', null=True, blank=True)
    ###
    recommendations = models.TextField(verbose_name='Рекомендации', max_length=4000, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

    
    def get_absolute_url(self):
       return reverse_lazy('monitoring_ket:monitoring-ket-detail', kwargs={"pk": self.pk})  

    def __str__(self):
        return f'{self.date}  -  {self.organization}'




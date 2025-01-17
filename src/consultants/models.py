from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy



class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user}'


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название организации',)
    farm = models.CharField(max_length=200, verbose_name='Название фермы(комплекса)',)
    manager = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Выбор менеджера данной организации', related_name='managed_organizations',)
    consultant = models.ForeignKey(Consultant, verbose_name='Консультант', on_delete=models.PROTECT, related_name='organizations')


    def __str__(self):
        return f'{self.name}  -  {self.farm}'


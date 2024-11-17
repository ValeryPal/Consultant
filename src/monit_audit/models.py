from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from user_app.models import Job
from consultants.models import Organization

class MonitAuditMilk(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='monitauditmilks', )
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, )
    content = models.CharField(verbose_name='Тип содержания', max_length=100, )
    livestock = models.IntegerField(verbose_name='Поголовье на ферме', )
    dairy_cattle = models.IntegerField(verbose_name='Количество дойного поголовья',  )
    days_lactation = models.IntegerField(verbose_name='Среднее количество дней лактации', )
    milk = models.IntegerField(verbose_name='Общий удой по ферме',  )
    milk_cow = models.FloatField(verbose_name='Удой на одну корову в сутки, кг', )
    milk_sales = models.IntegerField(verbose_name='Реализация молока в день',  )
    milk_fat = models.FloatField(verbose_name='Жирность молока, %',  )
    milk_protein = models.FloatField(verbose_name='Белок молока, %',  )
    milk_somatics = models.IntegerField(verbose_name='Соматика молока, тыс/мл',  )
    number_milkings = models.IntegerField(verbose_name='Количество доений',  )
    weight_cow = models.IntegerField(verbose_name='Вес взрослого животного',   )
    number_calvings = models.IntegerField(verbose_name='Количество отелов за месяц',  )
    calf_weight = models.IntegerField(verbose_name='Вес телят при рождении',  )
    groups = models.TextField(verbose_name='Разделение по группам', blank=True,  max_length=4000, )
    diet_composition = models.TextField(verbose_name='Состав рациона', blank=True,  max_length=4000, )
    diet_composition_feed = models.TextField(verbose_name='Состав комбикорма', blank=True,  max_length=4000, )
    notes_diet = models.TextField(verbose_name='Замечания по рациону', blank=True,  max_length=6000, )
    notes_animall = models.TextField(verbose_name='Замечания по животным', blank=True,  max_length=6000, )
    withdrawal = models.TextField(verbose_name='Выбытие(количество, причины)', blank=True, max_length=6000, )
    notes = models.TextField(verbose_name='Другие проблемы', blank=True,  max_length=6000, )
    offers = models.TextField(verbose_name='Предложения', blank=True,  max_length=6000, )
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, )

    def __str__(self):
        return f' {self.organization}'
    
    def get_absolute_url(self):
       return reverse_lazy('monit_audit:audit-detail', kwargs={"pk": self.pk})


from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from user_app.models import Job
from consultants.models import Organization

class MonitAuditCalves(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='monitauditcalvess', )
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, )
    content = models.CharField(verbose_name='Тип содержания', max_length=100, )
    livestock_calves = models.IntegerField(verbose_name='Количество телят в группе мониторинга', )
    weight_calves = models.IntegerField(verbose_name='Средний вес телят',   )
    number_boxes = models.IntegerField(verbose_name='Количество боксов для телят',  )
    number_calf = models.IntegerField(verbose_name='Количество телят 0-2 мес',  )
    number_milk = models.IntegerField(verbose_name='Количество поений молоком в сутки',  )
    calf_weight = models.IntegerField(verbose_name='Вес телят при рождении', )
    number_calvings = models.IntegerField(verbose_name='Количество отелов за месяц',)
    groups = models.TextField(verbose_name='Разделение по группам', blank=True,  max_length=4000, )
    diet_composition = models.TextField(verbose_name='Состав рациона', blank=True,  max_length=4000, )
    diet_composition_feed = models.TextField(verbose_name='Состав комбикорма', blank=True,  max_length=4000, )
    notes_diet = models.TextField(verbose_name='Замечания по рациону', blank=True,  max_length=6000, )
    notes_animall = models.TextField(verbose_name='Замечания по телятам', blank=True,  max_length=6000, )
    withdrawal = models.TextField(verbose_name='Выбытие(количество, причины)', blank=True, max_length=6000, )
    notes = models.TextField(verbose_name='Другие проблемы', blank=True,  max_length=6000, )
    offers = models.TextField(verbose_name='Предложения', blank=True,  max_length=6000, )
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, )

    def __str__(self):
        return f' {self.organization}'
    
    def get_absolute_url(self):
       return reverse_lazy('monit_calves:calves-detail', kwargs={"pk": self.pk})

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

def validate_percentage(value):
    """Валидатор для округления процентов до одной цифры после запятой."""
    if not (0 <= value <= 100):
        raise ValidationError(f'Значение {value} должно быть между 0 и 100.')
    return round(value, 1)

#  (мониторинг кормосмеси)
class MonitoringFeed(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='monitoringfeeds',)
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, null=True)   
    ###
    group = models.CharField(verbose_name='Группа животных', max_length=100, null=True)
    feed_1 = models.IntegerField(verbose_name='Количество остатков верхнего сита, гр.',)
    feed_2 = models.IntegerField(verbose_name='Количество остатков среднего сита, гр.',)
    feed_3 = models.IntegerField(verbose_name='Количество остатков нижнего сита, гр.',)
    feed_4 = models.IntegerField(verbose_name='Количество остатков дна, гр.',)
    summa = models.IntegerField(default=0, editable=False)
    percent_feed_1 = models.FloatField(default=0.0, validators=[validate_percentage], editable=False)
    percent_feed_2 = models.FloatField(default=0.0, validators=[validate_percentage], editable=False)
    percent_feed_3 = models.FloatField(default=0.0, validators=[validate_percentage], editable=False)
    percent_feed_4 = models.FloatField(default=0.0, validators=[validate_percentage], editable=False)
    ###
    foto_1 = models.ImageField(verbose_name='Вид(фото) верхнего сита 19 мм', upload_to='foto_monitoring/%Y/%m/%d', )      # фото верхнего сита 19 мм
    foto_2 = models.ImageField(verbose_name='Вид(фото) среднего сита 8 мм', upload_to='foto_monitoring/%Y/%m/%d', )     # фото среднего сита 8 мм
    foto_3 = models.ImageField(verbose_name='Вид(фото)нижнего сита 4 мм', upload_to='foto_monitoring/%Y/%m/%d', )      # фото нижнего сита 4 мм
    foto_4 = models.ImageField(verbose_name='Вид(фото) поддона', upload_to='foto_monitoring/%Y/%m/%d',)      # фото поддона
    feed_mixture = models.TextField(verbose_name='Замечания по кормосмеси',  null=True, blank=True)
    recommendations = models.TextField(verbose_name='Рекомендации', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

    def calculate_sum(self):
        """Вычисление суммы feed и сохранение в поле summa."""
        self.summa = self.feed_1 + self.feed_2 + self.feed_3 + self.feed_4

    def calculate_percentages(self):
        """Вычисление процентов для каждого feed и сохранение в соответствующие поля."""
        if self.summa != 0:
            self.percent_feed_1 = round((self.feed_1 / self.summa) * 100, 1)
            self.percent_feed_2 = round((self.feed_2 / self.summa) * 100, 1)
            self.percent_feed_3 = round((self.feed_3 / self.summa) * 100, 1)
            self.percent_feed_4 = round((self.feed_4 / self.summa) * 100, 1)
        else:
            self.percent_feed_1 = 0.0
            self.percent_feed_2 = 0.0
            self.percent_feed_3 = 0.0
            self.percent_feed_4 = 0.0

    def save(self, *args, **kwargs):
        """Сохранение измененного фото"""
        self.calculate_sum()
        self.calculate_percentages()
        if self.foto_1:
            self.foto_1 = compress_image(self.foto_1)
        if self.foto_2:
            self.foto_2 = compress_image(self.foto_2)
        if self.foto_3:
            self.foto_3 = compress_image(self.foto_3)
        if self.foto_4:
            self.foto_4 = compress_image(self.foto_4)
        super(MonitoringFeed, self).save(*args, **kwargs)


    def __str__(self):
        return f' {self.organization} (summa={self.summa}, percents=({self.percent_feed_1}, {self.percent_feed_2}, {self.percent_feed_3}, {self.percent_feed_4}))'

    def get_absolute_url(self):
       return reverse_lazy('monitoring:monitoringfeeds-detail', kwargs={"pk": self.pk})  

def compress_image(image, max_width=800, max_height=800):
    """Изменение фото по размеру и качеству"""
    img = PILImage.open(image)
    img.thumbnail((max_width, max_height), PILImage.Resampling.LANCZOS)

    img_io = BytesIO()
    img.save(img_io, format='JPEG', quality=140)
    new_image = ContentFile(img_io.getvalue(), name=image.name)
    
    return new_image




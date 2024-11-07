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
class Monitoring_nasko(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='monitoring_naskos',)
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, null=True)   
    ###
    group = models.CharField(verbose_name='Группа животных', max_length=100, null=True)
    feces_1 = models.IntegerField(verbose_name='Количество остатков верхнего сита, гр.',)
    feces_2 = models.IntegerField(verbose_name='Количество остатков среднего сита, гр.',)
    feces_3 = models.IntegerField(verbose_name='Количество остатков нижнего сита, гр.',)
    
    summa = models.IntegerField(default=0, editable=False)
    percent_feces_1 = models.FloatField(default=0.0, validators=[validate_percentage], editable=False)
    percent_feces_2 = models.FloatField(default=0.0, validators=[validate_percentage], editable=False)
    percent_feces_3 = models.FloatField(default=0.0, validators=[validate_percentage], editable=False)
    
    ###
    foto_1 = models.ImageField(verbose_name='Вид(фото) верхнего сита', upload_to='foto_monitoring_nasko/%Y/%m/%d', )      # фото верхнего сита 19 мм
    foto_2 = models.ImageField(verbose_name='Вид(фото) среднего сита', upload_to='foto_monitoring_nasko/%Y/%m/%d', )     # фото среднего сита 8 мм
    foto_3 = models.ImageField(verbose_name='Вид(фото)нижнего сита', upload_to='foto_monitoring_nasko/%Y/%m/%d', )      # фото нижнего сита 4 мм
    
    feces_mixture = models.TextField(verbose_name='Замечания', max_length=4000, null=True, blank=True)
    recommendations = models.TextField(verbose_name='Рекомендации', max_length=4000, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

    def calculate_sum(self):
        """Вычисление суммы feces и сохранение в поле summa."""
        self.summa = self.feces_1 + self.feces_2 + self.feces_3

    def calculate_percentages(self):
        """Вычисление процентов для каждого feces и сохранение в соответствующие поля."""
        if self.summa != 0:
            self.percent_feces_1 = round((self.feces_1 / self.summa) * 100, 1)
            self.percent_feces_2 = round((self.feces_2 / self.summa) * 100, 1)
            self.percent_feces_3 = round((self.feces_3 / self.summa) * 100, 1)
            
        else:
            self.percent_feces_1 = 0.0
            self.percent_feces_2 = 0.0
            self.percent_feces_3 = 0.0
           

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
        
        super(Monitoring_nasko, self).save(*args, **kwargs)


    def __str__(self):
        return f' {self.organization} (summa={self.summa}, percents=({self.percent_feces_1}, {self.percent_feces_2}, {self.percent_feces_3}))'

    def get_absolute_url(self):
       return reverse_lazy('monitoring_nasko:monitoring-nasko-detail', kwargs={"pk": self.pk})  

def compress_image(image, max_width=400, max_height=400):
    """Изменение фото по размеру и качеству"""
    img = PILImage.open(image)
    img.thumbnail((max_width, max_height), PILImage.Resampling.LANCZOS)

    img_io = BytesIO()
    img.save(img_io, format='JPEG', quality=65)
    new_image = ContentFile(img_io.getvalue(), name=image.name)
    
    return new_image




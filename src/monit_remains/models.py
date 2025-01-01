from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from consultants.models import Organization
from django.contrib.auth import get_user_model # вместо user
from user_app.models import Job

User = get_user_model()

#  (мониторинг остатков)
# class Remain(models.Model):
#     organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='remains',)
#     date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, null=True)   
    
#     products = models.TextField(verbose_name='Остатки продукции и количество',  null=True, blank=True)
#     created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
#     job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
#     user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

#     def get_absolute_url(self):
#        return reverse_lazy('monit_remains:monit-remains-detail', kwargs={"pk": self.pk}) 

#     def __str__(self):
#         return f'{self.date}  -  {self.products}'



class Remain(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Организация', related_name='remains',)
    date = models.DateField(verbose_name='Дата мониторинга', default=timezone.now, null=True)
    products_name_1 = models.CharField(verbose_name='Продукт 1', null=True, blank=True, max_length=30)
    products_name_2 = models.CharField(verbose_name='Продукт 2', null=True, blank=True, max_length=30)
    products_name_3 = models.CharField(verbose_name='Продукт 3', null=True, blank=True, max_length=30)
    products_name_4 = models.CharField(verbose_name='Продукт 4', null=True, blank=True, max_length=30)
    products_name_5 = models.CharField(verbose_name='Продукт 5', null=True, blank=True, max_length=30)
    products_1 = models.PositiveIntegerField(verbose_name='Количество продукта 1, кг', null=True, blank=True,)
    products_2 = models.PositiveIntegerField(verbose_name='Количество продукта 2, кг', null=True, blank=True, )
    products_3 = models.PositiveIntegerField(verbose_name='Количество продукта 3, кг', null=True, blank=True, )
    products_4 = models.PositiveIntegerField(verbose_name='Количество продукта 4, кг', null=True, blank=True, )
    products_5 = models.PositiveIntegerField(verbose_name='Количество продукта 5, кг', null=True, blank=True, )
    dose_products_1 = models.FloatField(verbose_name='Доза продукта 1 на одну голову, кг', null=True, blank=True)
    dose_products_2 = models.FloatField(verbose_name='Доза продукта 2 на одну голову, кг', null=True, blank=True)
    dose_products_3 = models.FloatField(verbose_name='Доза продукта 3 на одну голову, кг', null=True, blank=True)
    dose_products_4 = models.FloatField(verbose_name='Доза продукта 4 на одну голову, кг', null=True, blank=True)
    dose_products_5 = models.FloatField(verbose_name='Доза продукта 5 на одну голову, кг', null=True, blank=True)
    number_1 = models.PositiveIntegerField(verbose_name='Количество голов на "1" продукт', null=True, blank=True)
    number_2 = models.PositiveIntegerField(verbose_name='Количество голов на "2" продукт', null=True, blank=True)
    number_3 = models.PositiveIntegerField(verbose_name='Количество голов на "3" продукт', null=True, blank=True)
    number_4 = models.PositiveIntegerField(verbose_name='Количество голов на "4" продукт', null=True, blank=True)
    number_5 = models.PositiveIntegerField(verbose_name='Количество голов на "5" продукт', null=True, blank=True)
    comment = models.TextField(verbose_name='Коментарии',  null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now,)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name='Должность специалиста', null=True )
    user_name = models.CharField(verbose_name='ФИО', max_length=100, null=True)

    def get_absolute_url(self):
       return reverse_lazy('monit_remains:monit-remains-detail', kwargs={"pk": self.pk})

    def __str__(self):
        return f"Remain on {self.date} for {self.organization}"

    def days_until_exhaustion_product_1(self):
        """Calculate days until product 1 is exhausted."""
        if self.dose_products_1 > 0 and self.number_1 > 0:
            required_dose_1 = self.dose_products_1 * self.number_1
            return self.products_1 / required_dose_1
        return float('inf')  # Never exhaust

    def days_until_exhaustion_product_2(self):
        """Calculate days until product 2 is exhausted."""
        if self.dose_products_2 > 0 and self.number_2 > 0:
            required_dose_2 = self.dose_products_2 * self.number_2
            return self.products_2 / required_dose_2
        return float('inf')  # Never exhaust

    def days_until_exhaustion_product_3(self):
        """Calculate days until product 1 is exhausted."""
        if self.dose_products_3 > 0 and self.number_3 > 0:
            required_dose_3 = self.dose_products_3 * self.number_3
            return self.products_3 / required_dose_3
        return float('inf')  # Never exhaust
    
    def days_until_exhaustion_product_4(self):
        """Calculate days until product 1 is exhausted."""
        if self.dose_products_4 > 0 and self.number_4 > 0:
            required_dose_4 = self.dose_products_4 * self.number_4
            return self.products_4 / required_dose_4
        return float('inf')  # Never exhaust
    
    def days_until_exhaustion_product_5(self):
        """Calculate days until product 1 is exhausted."""
        if self.dose_products_5 > 0 and self.number_5 > 0:
            required_dose_5 = self.dose_products_5 * self.number_5
            return self.products_5 / required_dose_5
        return float('inf')  # Never exhaust
    

    def expiry_date_product_1(self):
        """Calculate the expiry date for product 1."""
        days_left = self.days_until_exhaustion_product_1()
        return self.date + timezone.timedelta(days=days_left)

    def expiry_date_product_2(self):
        """Calculate the expiry date for product 2."""
        days_left = self.days_until_exhaustion_product_2()
        return self.date + timezone.timedelta(days=days_left)
    
    def expiry_date_product_3(self):
        """Calculate the expiry date for product 2."""
        days_left = self.days_until_exhaustion_product_3()
        return self.date + timezone.timedelta(days=days_left)
    
    def expiry_date_product_4(self):
        """Calculate the expiry date for product 2."""
        days_left = self.days_until_exhaustion_product_4()
        return self.date + timezone.timedelta(days=days_left)
    
    def expiry_date_product_5(self):
        """Calculate the expiry date for product 2."""
        days_left = self.days_until_exhaustion_product_5()
        return self.date + timezone.timedelta(days=days_left)
    


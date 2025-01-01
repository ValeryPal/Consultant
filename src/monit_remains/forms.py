from django import forms
from .models import Remain

class RemainForm(forms.ModelForm):
    class Meta:
        model = Remain
        fields = ['date', 'comment',
                  'products_name_1', 'products_1', 'dose_products_1', 'number_1',
                  'products_name_2', 'products_2', 'dose_products_2', 'number_2',
                  'products_name_3', 'products_3', 'dose_products_3', 'number_3',
                  'products_name_4', 'products_4', 'dose_products_4', 'number_4',
                  'products_name_5', 'products_5', 'dose_products_5', 'number_5',
                  'job', 'user_name',]
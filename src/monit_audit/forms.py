from django import forms
from .models import MonitAuditMilk

class MonitAuditMilkForm(forms.ModelForm):
    class Meta:
        model = MonitAuditMilk
        fields = ['date', 'content', 'livestock', 'dairy_cattle', 'days_lactation',
                  'milk', 'milk_cow', 'milk_sales', 'milk_fat', 'milk_protein', 'milk_somatics',
                   'number_milkings', 'weight_cow', 'number_calvings', 'calf_weight',
                    'groups', 'offers_1', 'diet_composition', 'notes_diet', 'diet_composition_feed', 'offers_2',
                     'notes_animall', 'offers_3', 'withdrawal', 'offers_4',
                     'notes', 'offers', 'job', 'user_name']
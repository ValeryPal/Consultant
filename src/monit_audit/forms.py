from django import forms
from .models import MonitAuditMilk

class MonitAuditMilkForm(forms.ModelForm):
    class Meta:
        model = MonitAuditMilk
        fields = ['date', 'content', 'livestock', 'dairy_cattle', 'days_lactation',
                  'milk', 'milk_cow', 'milk_sales', 'milk_fat', 'milk_protein', 'milk_somatics',
                   'number_milkings', 'weight_cow', 'number_calvings', 'calf_weight',
                    'groups', 'diet_composition', 'diet_composition_feed', 'notes_diet',
                     'notes_animall', 'withdrawal', 'notes', 'offers', 'job', 'user_name']
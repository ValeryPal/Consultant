from django import forms
from .models import MonitAuditCalves

class MonitAuditCalvesForm(forms.ModelForm):
    class Meta:
        model = MonitAuditCalves
        fields = ['date', 'content', 'livestock_calves', 'weight_calves', 'number_boxes',
                  'number_calf', 'number_milk', 'calf_weight', 'number_calvings',
                    'groups', 'offers_1', 'diet_composition', 'notes_diet', 'diet_composition_feed', 'offers_2',
                     'notes_animall', 'offers_3', 'withdrawal', 'offers_4', 'notes', 'offers', 'job', 'user_name']
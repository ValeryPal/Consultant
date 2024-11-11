from django import forms
from .models import MonitAuditCalves

class MonitAuditCalvesForm(forms.ModelForm):
    class Meta:
        model = MonitAuditCalves
        fields = ['date', 'content', 'livestock_calves', 'weight_calves', 'number_boxes',
                  'number_calf', 'number_milk', 'calf_weight', 'number_calvings',
                    'groups', 'diet_composition', 'diet_composition_feed', 'notes_diet',
                     'notes_animall', 'withdrawal', 'notes', 'offers', 'job', 'user_name']
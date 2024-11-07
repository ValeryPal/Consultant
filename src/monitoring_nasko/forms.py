from django import forms
from .models import Monitoring_nasko

class Monitoring_naskoForm(forms.ModelForm):
    class Meta:
        model = Monitoring_nasko
        fields = ['date', 'group', 'feces_1', 'feces_2', 'feces_3',
              'foto_1', 'foto_2', 'foto_3',
              'feces_mixture', 'recommendations', 'job', 'user_name']
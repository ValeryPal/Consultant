from django import forms
from .models import Monitoring_ph

class Monitoring_phForm(forms.ModelForm):
    class Meta:
        model = Monitoring_ph
        fields = ['date', 'group', 'animal_1', 'animal_2', 'animal_3', 'animal_4',
              'animal_5', 'animal_6', 'animal_7', 'animal_8', 'animal_9', 'animal_10',
              'ph_1', 'ph_2', 'ph_3', 'ph_4',
              'ph_5', 'ph_6', 'ph_7', 'ph_8', 'ph_9', 'ph_10',
              'recommendations', 'job', 'user_name']
from django import forms
from .models import Monitoring_ph

class Monitoring_phForm(forms.ModelForm):
    class Meta:
        model = Monitoring_ph
        fields = ['date', 'group',
                  'animal_1', 'calving_1', 'ph_1',
                  'animal_2', 'calving_2', 'ph_2',
                  'animal_3', 'calving_3', 'ph_3',
                  'animal_4', 'calving_4', 'ph_4', 
                  'animal_5', 'calving_5', 'ph_5',
                  'animal_6', 'calving_6', 'ph_6',
                  'animal_7', 'calving_7', 'ph_7',
                  'animal_8', 'calving_8', 'ph_8',
                  'animal_9', 'calving_9', 'ph_9', 
                  'animal_10', 'calving_10', 'ph_10',
                  'recommendations', 'job', 'user_name']
from django import forms
from .models import Monitoring_ket

class Monitoring_ketForm(forms.ModelForm):
    class Meta:
        model = Monitoring_ket
        fields = ['date', 'group',
                  'animal_1', 'keton_1',
                  'animal_2', 'keton_2',
                  'animal_3', 'keton_3',
                  'animal_4', 'keton_4',
                  'animal_5', 'keton_5',
                  'animal_6', 'keton_6',
                  'animal_7', 'keton_7',
                  'animal_8', 'keton_8',
                  'animal_9', 'keton_9',
                  'animal_10', 'keton_10',
                  'animal_11', 'keton_11',
                  'animal_12', 'keton_12',
                  'animal_13', 'keton_13',
                  'animal_14', 'keton_14',
                  'animal_15', 'keton_15',
                  'recommendations', 'job', 'user_name']
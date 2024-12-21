from django import forms
from .models import Remain

class RemainForm(forms.ModelForm):
    class Meta:
        model = Remain
        fields = ['date', 'user_name', 'products']
from django import forms
from .models import MonitoringFeed

class MonitoringForm(forms.ModelForm):
    class Meta:
        model = MonitoringFeed
        fields = ['date',
              'foto_1', 'foto_2', 'foto_3', 'foto_4',
              'feed_mixture', 'job', 'user_name']
from django import forms
from .models import MonitoringFeed

class MonitoringForm(forms.ModelForm):
    class Meta:
        model = MonitoringFeed
        fields = ['date', 'group', 'feed_1', 'feed_2', 'feed_3', 'feed_4',
              'foto_1', 'foto_2', 'foto_3', 'foto_4',
              'feed_mixture', 'recommendations', 'job', 'user_name']
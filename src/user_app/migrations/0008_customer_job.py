# Generated by Django 5.0.7 on 2024-10-16 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_job_remove_customer_additional_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='user_app.job', verbose_name='Должность'),
        ),
    ]

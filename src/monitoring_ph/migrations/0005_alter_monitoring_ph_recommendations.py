# Generated by Django 5.0.7 on 2024-11-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_ph', '0004_alter_monitoring_ph_recommendations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoring_ph',
            name='recommendations',
            field=models.TextField(blank=True, null=True, verbose_name='Рекомендации'),
        ),
    ]
# Generated by Django 5.0.7 on 2024-11-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_alter_monitoringfeed_feed_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoringfeed',
            name='recommendations',
            field=models.TextField(max_length=4000, null=True, verbose_name='Рекомендации'),
        ),
    ]

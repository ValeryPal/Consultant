# Generated by Django 5.0.7 on 2024-11-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_alter_monitoringfeed_feed_mixture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringfeed',
            name='feed_mixture',
            field=models.TextField(blank=True, null=True, verbose_name='Замечания по кормосмеси'),
        ),
        migrations.AlterField(
            model_name='monitoringfeed',
            name='recommendations',
            field=models.TextField(blank=True, null=True, verbose_name='Рекомендации'),
        ),
    ]

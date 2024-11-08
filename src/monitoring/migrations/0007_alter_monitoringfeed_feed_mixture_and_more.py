# Generated by Django 5.0.7 on 2024-11-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0006_alter_monitoringfeed_foto_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringfeed',
            name='feed_mixture',
            field=models.TextField(blank=True, max_length=4000, null=True, verbose_name='Замечания по кормосмеси'),
        ),
        migrations.AlterField(
            model_name='monitoringfeed',
            name='recommendations',
            field=models.TextField(blank=True, max_length=4000, null=True, verbose_name='Рекомендации'),
        ),
    ]

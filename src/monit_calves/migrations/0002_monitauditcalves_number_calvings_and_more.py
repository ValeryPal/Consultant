# Generated by Django 5.0.7 on 2024-11-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monit_calves', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitauditcalves',
            name='number_calvings',
            field=models.IntegerField(null=True, verbose_name='Количество отелов за месяц'),
        ),
        migrations.AlterField(
            model_name='monitauditcalves',
            name='livestock_calves',
            field=models.IntegerField(verbose_name='Количество телят в группе мониторинга'),
        ),
    ]

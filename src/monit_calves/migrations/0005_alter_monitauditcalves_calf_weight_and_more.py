# Generated by Django 5.0.7 on 2024-11-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monit_calves', '0004_alter_monitauditcalves_calf_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitauditcalves',
            name='calf_weight',
            field=models.IntegerField(verbose_name='Вес телят при рождении'),
        ),
        migrations.AlterField(
            model_name='monitauditcalves',
            name='number_calvings',
            field=models.IntegerField(verbose_name='Количество отелов за месяц'),
        ),
    ]

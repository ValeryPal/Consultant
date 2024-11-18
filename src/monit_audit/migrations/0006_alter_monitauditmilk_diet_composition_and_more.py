# Generated by Django 5.0.7 on 2024-11-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monit_audit', '0005_alter_monitauditmilk_milk_cow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitauditmilk',
            name='diet_composition',
            field=models.TextField(blank=True, max_length=4000, verbose_name='Состав рациона'),
        ),
        migrations.AlterField(
            model_name='monitauditmilk',
            name='diet_composition_feed',
            field=models.TextField(blank=True, max_length=4000, verbose_name='Состав комбикорма'),
        ),
        migrations.AlterField(
            model_name='monitauditmilk',
            name='groups',
            field=models.TextField(blank=True, max_length=4000, verbose_name='Разделение по группам'),
        ),
        migrations.AlterField(
            model_name='monitauditmilk',
            name='notes',
            field=models.TextField(blank=True, max_length=6000, verbose_name='Другие проблемы'),
        ),
        migrations.AlterField(
            model_name='monitauditmilk',
            name='notes_animall',
            field=models.TextField(blank=True, max_length=6000, verbose_name='Замечания по животным'),
        ),
        migrations.AlterField(
            model_name='monitauditmilk',
            name='notes_diet',
            field=models.TextField(blank=True, max_length=6000, verbose_name='Замечания по рациону'),
        ),
        migrations.AlterField(
            model_name='monitauditmilk',
            name='offers',
            field=models.TextField(blank=True, max_length=6000, verbose_name='Предложения'),
        ),
        migrations.AlterField(
            model_name='monitauditmilk',
            name='withdrawal',
            field=models.TextField(blank=True, max_length=6000, verbose_name='Выбытие(количество, причины)'),
        ),
    ]
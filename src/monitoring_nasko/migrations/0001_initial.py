# Generated by Django 5.0.7 on 2024-11-07 09:19

import django.db.models.deletion
import django.utils.timezone
import monitoring_nasko.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultants', '0017_alter_organization_consultant_and_more'),
        ('user_app', '0014_personalaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoring_nasko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Дата мониторинга')),
                ('group', models.CharField(max_length=100, null=True, verbose_name='Группа животных')),
                ('feces_1', models.IntegerField(verbose_name='Количество остатков верхнего сита, гр.')),
                ('feces_2', models.IntegerField(verbose_name='Количество остатков среднего сита, гр.')),
                ('feces_3', models.IntegerField(verbose_name='Количество остатков нижнего сита, гр.')),
                ('summa', models.IntegerField(default=0, editable=False)),
                ('percent_feces_1', models.FloatField(default=0.0, editable=False, validators=[monitoring_nasko.models.validate_percentage])),
                ('percent_feces_2', models.FloatField(default=0.0, editable=False, validators=[monitoring_nasko.models.validate_percentage])),
                ('percent_feces_3', models.FloatField(default=0.0, editable=False, validators=[monitoring_nasko.models.validate_percentage])),
                ('foto_1', models.ImageField(upload_to='foto_monitoring_nasko/%Y/%m/%d', verbose_name='Вид(фото) верхнего сита')),
                ('foto_2', models.ImageField(upload_to='foto_monitoring_nasko/%Y/%m/%d', verbose_name='Вид(фото) среднего сита')),
                ('foto_3', models.ImageField(upload_to='foto_monitoring_nasko/%Y/%m/%d', verbose_name='Вид(фото)нижнего сита')),
                ('feces_mixture', models.TextField(blank=True, max_length=4000, null=True, verbose_name='Замечания')),
                ('recommendations', models.TextField(blank=True, max_length=4000, null=True, verbose_name='Рекомендации')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания записи')),
                ('user_name', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user_app.job', verbose_name='Должность специалиста')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='monitoring_naskos', to='consultants.organization', verbose_name='Организация')),
            ],
        ),
    ]
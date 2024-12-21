# Generated by Django 5.0.7 on 2024-12-21 16:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultants', '0020_alter_organization_farm_alter_organization_manager_and_more'),
        ('user_app', '0015_alter_job_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Дата мониторинга')),
                ('products', models.TextField(blank=True, null=True, verbose_name='Остатки продукции и количество')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания записи')),
                ('user_name', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user_app.job', verbose_name='Должность специалиста')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='remains', to='consultants.organization', verbose_name='Организация')),
            ],
        ),
    ]

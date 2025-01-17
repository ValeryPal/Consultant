# Generated by Django 5.0.7 on 2024-10-30 17:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0005_remove_consultant_user_remove_manager_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_organizations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='consultant',
            name='user',
        ),
        migrations.AlterField(
            model_name='organization',
            name='consultant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='consultants.consultant', verbose_name='Консультант'),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.AddField(
            model_name='consultant',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

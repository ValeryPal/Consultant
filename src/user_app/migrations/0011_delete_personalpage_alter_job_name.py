# Generated by Django 5.0.7 on 2024-10-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0010_alter_customer_first_name_alter_customer_last_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalPage',
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Должность'),
        ),
    ]

# Generated by Django 5.0.7 on 2024-11-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0005_monitoringfeed_group_alter_monitoringfeed_feed_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringfeed',
            name='foto_1',
            field=models.ImageField(upload_to='foto_monitoring/%Y/%m/%d', verbose_name='Вид(фото) верхнего сита 19 мм'),
        ),
    ]

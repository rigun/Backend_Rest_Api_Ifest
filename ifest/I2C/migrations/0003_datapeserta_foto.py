# Generated by Django 2.0.1 on 2018-01-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('I2C', '0002_auto_20180108_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapeserta',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]

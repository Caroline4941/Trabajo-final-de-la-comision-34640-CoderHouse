# Generated by Django 4.1.3 on 2023-01-06 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_alter_avatar_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='autor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='cuerpo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 16, 54, 56, 130872)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitulo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=20),
        ),
    ]

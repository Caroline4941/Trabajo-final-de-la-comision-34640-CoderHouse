# Generated by Django 4.1.3 on 2023-01-04 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0005_perfil'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perfil',
            new_name='User',
        ),
    ]

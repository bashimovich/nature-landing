# Generated by Django 4.0.1 on 2022-11-16 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature', '0009_gallerypagegallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carusel',
            name='item',
            field=models.CharField(choices=[('1', 'carusel 1'), ('2', 'carusel 2'), ('3', 'carusel 3'), ('4', 'carusel 4'), ('5', 'carusel 5')], default='1', max_length=10),
        ),
    ]
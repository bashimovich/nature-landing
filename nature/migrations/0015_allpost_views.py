# Generated by Django 4.0.1 on 2022-11-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature', '0014_allpost_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='allpost',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

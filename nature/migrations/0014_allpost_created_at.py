# Generated by Django 4.0.1 on 2022-11-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature', '0013_alter_allpost_destrict'),
    ]

    operations = [
        migrations.AddField(
            model_name='allpost',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
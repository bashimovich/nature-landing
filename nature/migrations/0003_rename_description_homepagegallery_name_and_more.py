# Generated by Django 4.0.1 on 2022-11-15 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nature', '0002_homepagegallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepagegallery',
            old_name='description',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='homepagegallery',
            name='title',
        ),
    ]

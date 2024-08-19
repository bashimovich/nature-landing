# Generated by Django 4.0.1 on 2022-11-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nature', '0015_allpost_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allpost',
            name='category',
            field=models.CharField(choices=[('monument', 'Monument'), ('reserve', 'Reserve'), ('resources', 'Natural Resources')], default='monument', max_length=100),
        ),
        migrations.AlterField(
            model_name='allpost',
            name='destrict',
            field=models.CharField(choices=[('mary', 'Mary'), ('lebap', 'Lebap'), ('ahal', 'Ahal'), ('balkan', 'Balkan'), ('dasoguz', 'Dashoguz')], default='mary', max_length=100),
        ),
    ]
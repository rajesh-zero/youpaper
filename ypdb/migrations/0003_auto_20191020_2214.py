# Generated by Django 2.2.6 on 2019-10-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ypdb', '0002_watched'),
    ]

    operations = [
        migrations.AddField(
            model_name='ypdb',
            name='ypdb_genre',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='ypdb',
            name='ypdb_plot',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='ypdb',
            name='ypdb_runtime',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='ypdb',
            name='ypdb_seasons',
            field=models.CharField(default='', max_length=300),
        ),
    ]
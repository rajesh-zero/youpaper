# Generated by Django 2.2.6 on 2019-10-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ypdb', '0003_auto_20191020_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ypdb',
            name='ypdb_plot',
            field=models.CharField(default='', max_length=20000),
        ),
    ]

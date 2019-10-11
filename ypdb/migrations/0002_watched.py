# Generated by Django 2.2.6 on 2019-10-10 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
        ('ypdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watched',
            fields=[
                ('watched_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
                ('ypdb_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ypdb.Ypdb')),
            ],
        ),
    ]
# Generated by Django 2.1.3 on 2018-11-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysConfig',
            fields=[
                ('ID', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('Content', models.CharField(max_length=5000)),
                ('ConfigType', models.IntegerField()),
                ('Updated', models.DateTimeField(default=1541577588.0640576)),
            ],
        ),
    ]

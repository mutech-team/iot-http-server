# Generated by Django 3.0.7 on 2020-07-03 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_data_serialized'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='serialized',
        ),
    ]
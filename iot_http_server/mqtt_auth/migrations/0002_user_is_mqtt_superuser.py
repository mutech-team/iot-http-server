# Generated by Django 3.0.6 on 2020-05-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_mqtt_superuser',
            field=models.BooleanField(default=False),
        ),
    ]

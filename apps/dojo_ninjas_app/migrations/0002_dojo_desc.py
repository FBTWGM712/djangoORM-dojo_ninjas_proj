# Generated by Django 2.2.4 on 2021-03-05 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='TEMP', max_length=255),
        ),
    ]

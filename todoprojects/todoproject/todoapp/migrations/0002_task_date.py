# Generated by Django 4.2.1 on 2023-06-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default='1990-03-22'),
            preserve_default=False,
        ),
    ]

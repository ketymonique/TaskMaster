# Generated by Django 5.1.1 on 2024-10-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

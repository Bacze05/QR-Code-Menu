# Generated by Django 5.0.2 on 2024-02-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='orden',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-13 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_categoria_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]

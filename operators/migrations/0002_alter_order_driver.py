# Generated by Django 4.2.5 on 2024-01-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Drivers', '0001_initial'),
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Drivers.driver'),
        ),
    ]

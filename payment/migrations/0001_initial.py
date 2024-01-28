# Generated by Django 4.2.5 on 2024-01-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operators', '0002_alter_order_driver'),
        ('Drivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField()),
                ('type', models.CharField(choices=[('naxt', 'naxt'), ('karta', 'karta')], max_length=30)),
                ('date', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Drivers.driver')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operators.operator')),
            ],
        ),
    ]

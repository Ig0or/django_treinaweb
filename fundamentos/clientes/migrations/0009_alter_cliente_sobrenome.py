# Generated by Django 3.2.8 on 2021-12-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20211202_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=30),
        ),
    ]

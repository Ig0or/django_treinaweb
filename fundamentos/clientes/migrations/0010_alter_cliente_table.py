# Generated by Django 3.2.8 on 2021-12-02 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_alter_cliente_sobrenome'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cliente',
            table='cliente_sistema',
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagoscredito',
            name='entidadAprobacion',
            field=models.CharField(choices=[('AX', 'AMERICANEXPRESS'), ('CA', 'MASTERCARD'), ('VI', 'VISA')], max_length=1),
        ),
    ]
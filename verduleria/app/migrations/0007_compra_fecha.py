# Generated by Django 2.0.13 on 2019-04-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_compra_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
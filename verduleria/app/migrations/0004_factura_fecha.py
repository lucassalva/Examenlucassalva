# Generated by Django 2.0.13 on 2019-04-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190411_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='fecha',
            field=models.DateField(blank=True, null=True),
            preserve_default=False,
        ),
    ]

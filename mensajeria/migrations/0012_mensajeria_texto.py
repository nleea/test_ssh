# Generated by Django 4.2 on 2023-07-17 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0011_alter_peticion_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajeria',
            name='texto',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0019_mensajeria_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajeria',
            name='voice',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

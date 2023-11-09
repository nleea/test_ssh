# Generated by Django 4.2.3 on 2023-07-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajeria', '0015_rename_multimedia_mensajeria_sha256_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensajeria',
            name='mime_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mensajeria',
            name='multimedia_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mensajeria',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.6 on 2022-11-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_bulkimport_staffid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default=' ', max_length=70),
        ),
    ]

# Generated by Django 3.0.6 on 2022-11-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_auto_20221127_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkimport',
            name='filename',
            field=models.FileField(upload_to=''),
        ),
    ]

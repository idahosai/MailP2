# Generated by Django 3.0.6 on 2022-11-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20221126_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachedtag',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.0.6 on 2023-02-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_auto_20230201_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfeild',
            name='customfeildintvalue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='userid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
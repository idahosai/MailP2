# Generated by Django 3.0.6 on 2022-11-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20221126_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='numberofsubscribes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='numberofunsubscribes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='totalsubscribes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

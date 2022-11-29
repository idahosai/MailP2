# Generated by Django 3.0.6 on 2022-11-29 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20221129_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='bulkimportid',
        ),
        migrations.AddField(
            model_name='bulkimport',
            name='attachedcustomfeildid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Attachedcustomfeild'),
        ),
        migrations.AddField(
            model_name='bulkimport',
            name='attachedformid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.AttachedForm'),
        ),
        migrations.AddField(
            model_name='bulkimport',
            name='attachedgroupid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Attachedgroup'),
        ),
        migrations.AddField(
            model_name='bulkimport',
            name='attachedtagid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Attachedtag'),
        ),
    ]

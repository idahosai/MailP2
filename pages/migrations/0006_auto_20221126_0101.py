# Generated by Django 3.0.6 on 2022-11-26 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_attachedcustomfeildfrombulkimport_attachedgroupfrombulkimport_attachedtagfrombulkimport_bulkimport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachedgroupfrombulkimport',
            name='bulkimportid',
        ),
        migrations.RemoveField(
            model_name='attachedgroupfrombulkimport',
            name='groupid',
        ),
        migrations.RemoveField(
            model_name='attachedtagfrombulkimport',
            name='bulkimportid',
        ),
        migrations.RemoveField(
            model_name='attachedtagfrombulkimport',
            name='tagid',
        ),
        migrations.AddField(
            model_name='contact',
            name='bulkimportid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Bulkimport'),
        ),
        migrations.AddField(
            model_name='contact',
            name='staffid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Staff'),
        ),
        migrations.DeleteModel(
            name='Attachedcustomfeildfrombulkimport',
        ),
        migrations.DeleteModel(
            name='Attachedgroupfrombulkimport',
        ),
        migrations.DeleteModel(
            name='Attachedtagfrombulkimport',
        ),
    ]

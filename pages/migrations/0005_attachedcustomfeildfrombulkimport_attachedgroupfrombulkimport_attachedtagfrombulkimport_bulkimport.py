# Generated by Django 3.0.6 on 2022-11-25 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20221123_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulkimport',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('importlocation', models.CharField(max_length=70)),
                ('details', models.CharField(max_length=70)),
                ('status', models.CharField(max_length=70)),
                ('datetime', models.DateTimeField(null=True)),
                ('whatshouldwedo', models.CharField(max_length=70)),
                ('notifywhenreviewcompleted', models.CharField(max_length=70)),
                ('notifywhenreviewcompletedyesbox', models.CharField(max_length=70)),
                ('howsubscribersacquired', models.CharField(max_length=70)),
                ('howsubscribersacquiredotherbox', models.CharField(max_length=70)),
                ('anotheremailprovider', models.CharField(max_length=70)),
                ('anotheremailprovideryesdropdown', models.CharField(max_length=70)),
                ('filename', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Attachedtagfrombulkimport',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('dateofattachement', models.DateTimeField(null=True)),
                ('bulkimportid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Bulkimport')),
                ('tagid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Attachedgroupfrombulkimport',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('dateofattachement', models.DateTimeField(null=True)),
                ('bulkimportid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Bulkimport')),
                ('groupid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Attachedcustomfeildfrombulkimport',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('dateofattachement', models.DateTimeField(null=True)),
                ('Customfeildid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Customfeild')),
                ('bulkimportid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Bulkimport')),
            ],
        ),
    ]
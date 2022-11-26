# Generated by Django 3.0.6 on 2022-11-23 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('dateofcreation', models.DateTimeField(null=True)),
                ('status', models.CharField(max_length=70)),
                ('numberofsubscribes', models.IntegerField()),
                ('totalsubscribes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('dateofcreation', models.DateTimeField(null=True)),
                ('type', models.CharField(max_length=70)),
                ('numberofsubscribes', models.IntegerField()),
                ('numberofunsubscribes', models.IntegerField()),
                ('totalsubscribes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Attachedgroup',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('dateofattachement', models.DateTimeField(null=True)),
                ('contactid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Contact')),
                ('groupid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Group')),
            ],
        ),
        migrations.CreateModel(
            name='AttachedForm',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('dateofattachement', models.DateTimeField(null=True)),
                ('contactid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Contact')),
                ('formid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Form')),
            ],
        ),
    ]

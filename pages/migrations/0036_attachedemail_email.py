# Generated by Django 3.0.6 on 2023-11-21 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0035_attachedsegment_staffid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=' ', max_length=70)),
                ('numberofcontactssentto', models.IntegerField(blank=True, null=True)),
                ('dateofcreation', models.DateTimeField(null=True)),
                ('subjecttitle', models.CharField(default=' ', max_length=70)),
                ('opens', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'unique_together': {('id', 'name', 'numberofcontactssentto', 'dateofcreation', 'subjecttitle', 'opens')},
            },
        ),
        migrations.CreateModel(
            name='Attachedemail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateofattachement', models.DateTimeField(null=True)),
                ('emailid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Email')),
                ('staffid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Staff')),
            ],
            options={
                'unique_together': {('id', 'dateofattachement', 'emailid', 'staffid')},
            },
        ),
    ]

# Generated by Django 3.0.6 on 2023-09-27 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0031_attachedsegment_segment'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinStaffContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contactid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Contact')),
                ('staffid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Staff')),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2022-11-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_auto_20221129_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulkimport',
            name='attachedcustomfeildid',
        ),
        migrations.RemoveField(
            model_name='bulkimport',
            name='attachedformid',
        ),
        migrations.RemoveField(
            model_name='bulkimport',
            name='attachedgroupid',
        ),
        migrations.RemoveField(
            model_name='bulkimport',
            name='attachedtagid',
        ),
        migrations.CreateModel(
            name='AttachedAll',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('dateofattachement', models.DateTimeField(null=True)),
                ('attachedcustomfeildid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Attachedcustomfeild')),
                ('attachedformid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.AttachedForm')),
                ('attachedgroupid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Attachedgroup')),
                ('attachedtagid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Attachedtag')),
            ],
        ),
        migrations.AddField(
            model_name='bulkimport',
            name='attachedall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.AttachedAll'),
        ),
    ]

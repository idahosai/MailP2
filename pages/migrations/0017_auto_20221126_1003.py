# Generated by Django 3.0.6 on 2022-11-26 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_tag_type'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attachedtag',
            unique_together={('id', 'dateofattachement', 'contactid', 'tagid')},
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('id', 'name', 'dateofcreation', 'type')},
        ),
    ]

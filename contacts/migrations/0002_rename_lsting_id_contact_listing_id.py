# Generated by Django 4.2.6 on 2023-11-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='lsting_id',
            new_name='listing_id',
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_auto_20201024_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bids',
            old_name='player',
            new_name='p_id',
        ),
        migrations.RenameField(
            model_name='bids',
            old_name='team',
            new_name='team_name',
        ),
    ]

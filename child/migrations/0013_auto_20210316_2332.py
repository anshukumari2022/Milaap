# Generated by Django 2.2.6 on 2021-03-16 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0012_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='perms',
            new_name='trained',
        ),
        migrations.RemoveField(
            model_name='member',
            name='uperms',
        ),
        migrations.DeleteModel(
            name='phone',
        ),
    ]

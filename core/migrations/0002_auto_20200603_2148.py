# Generated by Django 3.0.6 on 2020-06-03 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='long',
            new_name='lng',
        ),
    ]
# Generated by Django 4.1.6 on 2023-05-23 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poem',
            old_name='autor',
            new_name='author',
        ),
    ]
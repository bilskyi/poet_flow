# Generated by Django 4.1.6 on 2023-06-20 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpoem',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userpoem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.tags'),
        ),
        migrations.AddField(
            model_name='poet',
            name='poems',
            field=models.ManyToManyField(blank=True, to='home.classicpoem'),
        ),
        migrations.AddField(
            model_name='classicpoem',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.poet'),
        ),
        migrations.AddField(
            model_name='classicpoem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='home.tags'),
        ),
    ]
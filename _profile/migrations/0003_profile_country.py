# Generated by Django 3.1.2 on 2021-09-04 10:12

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('_profile', '0002_auto_20210830_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]

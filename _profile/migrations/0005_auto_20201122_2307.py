# Generated by Django 3.1.2 on 2020-11-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_profile', '0004_auto_20201122_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 3.1.2 on 2021-03-02 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_auto_20201128_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectitem',
            name='tag',
        ),
    ]

# Generated by Django 3.1.2 on 2021-03-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_profile', '0018_portfoliotemplate_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliotemplate',
            name='paid',
            field=models.BooleanField(default=True),
        ),
    ]

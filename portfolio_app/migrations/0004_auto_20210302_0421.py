# Generated by Django 3.1.2 on 2021-03-02 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_remove_projectitem_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-08 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

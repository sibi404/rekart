# Generated by Django 4.2.5 on 2023-11-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_plasticwaste_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]

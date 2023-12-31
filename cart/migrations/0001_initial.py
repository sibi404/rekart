# Generated by Django 4.2.5 on 2023-11-16 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_plasticwaste_seller'),
        ('accounts', '0002_alter_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='accounts.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cartlist')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.products')),
            ],
        ),
    ]

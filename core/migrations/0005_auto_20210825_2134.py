# Generated by Django 3.2.6 on 2021-08-25 16:04

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210825_0039'),
        ('core', '0004_alter_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Transaction_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(blank=True, choices=[('cod', 'Cash On Delivery'), ('googlepay', 'GPay'), ('paytm', 'Paytm'), ('banktransfer', 'Bank Transfer')], max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customerprofile'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(default=core.models.all_item, to='core.OrderItem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
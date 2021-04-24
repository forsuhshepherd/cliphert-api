# Generated by Django 3.1.3 on 2021-04-22 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210422_1334'),
        ('orders', '0003_auto_20210422_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.paymentmethod'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('paid', 'paid'), ('processing', 'processing'), ('cancelled', 'cancelled'), ('refunded', 'refunded')], default='Undefined', max_length=20),
        ),
    ]

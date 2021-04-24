# Generated by Django 3.1.3 on 2021-04-22 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210422_1334'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.paymentmethod'),
            preserve_default=False,
        ),
    ]

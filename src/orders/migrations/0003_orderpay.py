# Generated by Django 5.1 on 2024-10-14 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_phone', models.CharField(max_length=11)),
                ('pay_image', models.ImageField(upload_to='vodafone_cash')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

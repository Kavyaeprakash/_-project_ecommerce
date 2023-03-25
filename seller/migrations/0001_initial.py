# Generated by Django 4.1.7 on 2023-03-10 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=100)),
                ('product_category', models.CharField(max_length=50)),
                ('product_no', models.BigIntegerField()),
                ('product_stock', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='product/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
            options={
                'db_table': 'product_tb',
            },
        ),
    ]

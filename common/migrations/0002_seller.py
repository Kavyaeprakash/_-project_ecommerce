# Generated by Django 4.1.7 on 2023-03-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_email', models.CharField(max_length=50)),
                ('s_address', models.CharField(max_length=100)),
                ('s_mobile', models.BigIntegerField()),
                ('s_username', models.IntegerField(default=0)),
                ('s_password', models.CharField(max_length=50)),
                ('s_bank_name', models.CharField(max_length=50)),
                ('s_bank_branch', models.CharField(max_length=50)),
                ('s_ifsc_code', models.CharField(max_length=50)),
                ('s_acc_number', models.BigIntegerField()),
                ('s_image', models.ImageField(upload_to='seller/')),
                ('s_status', models.CharField(default='pending', max_length=20)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
    ]

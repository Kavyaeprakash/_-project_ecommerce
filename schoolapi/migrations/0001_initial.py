# Generated by Django 4.1.7 on 2023-03-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_dob', models.CharField(max_length=50)),
                ('s_email', models.CharField(max_length=50)),
                ('s_phone', models.BigIntegerField()),
                ('s_password', models.CharField(max_length=50)),
            ],
        ),
    ]
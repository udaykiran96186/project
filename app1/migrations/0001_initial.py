# Generated by Django 3.2.7 on 2021-11-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('emailId', models.EmailField(max_length=100, unique=True)),
                ('mobileNumber', models.IntegerField(unique=True)),
                ('address', models.TextField(max_length=250)),
            ],
        ),
    ]

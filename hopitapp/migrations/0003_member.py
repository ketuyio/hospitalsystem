# Generated by Django 3.2.24 on 2024-02-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopitapp', '0002_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
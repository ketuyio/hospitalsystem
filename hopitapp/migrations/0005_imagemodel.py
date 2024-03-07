# Generated by Django 3.2.24 on 2024-03-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopitapp', '0004_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
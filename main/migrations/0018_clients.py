# Generated by Django 4.2 on 2023-05-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_delete_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30, verbose_name='name')),
                ('client_img', models.ImageField(upload_to='images', verbose_name='client image')),
                ('client_proff', models.CharField(max_length=30, verbose_name='professional')),
                ('client_info', models.TextField(verbose_name='info about client')),
            ],
        ),
    ]

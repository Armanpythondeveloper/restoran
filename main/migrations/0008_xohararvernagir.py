# Generated by Django 4.2 on 2023-05-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_xohararner'),
    ]

    operations = [
        migrations.CreateModel(
            name='XohararVernagir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vern_1', models.TextField(verbose_name='vernagir 1')),
                ('vern_2', models.TextField(verbose_name='vernagir 2')),
            ],
        ),
    ]

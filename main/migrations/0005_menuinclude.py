# Generated by Django 4.2 on 2023-05-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_includeindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuInclude',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('men_1', models.TextField(verbose_name='men 1')),
                ('men_2', models.TextField(verbose_name='men 2')),
                ('men_3', models.TextField(verbose_name='men 3')),
                ('men_4', models.TextField(verbose_name='men 4')),
                ('men_5', models.TextField(verbose_name='men 5')),
                ('men_6', models.TextField(verbose_name='men 6')),
                ('men_7', models.TextField(verbose_name='men 7')),
                ('men_8', models.TextField(verbose_name='men 8')),
            ],
        ),
    ]

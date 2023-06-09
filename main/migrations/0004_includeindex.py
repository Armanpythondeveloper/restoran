# Generated by Django 4.2 on 2023-05-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_indexsecondinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncludeIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_1', models.ImageField(upload_to='images', verbose_name='image1')),
                ('img_2', models.ImageField(upload_to='images', verbose_name='image2')),
                ('img_3', models.ImageField(upload_to='images', verbose_name='image3')),
                ('img_4', models.ImageField(upload_to='images', verbose_name='image4')),
                ('name', models.CharField(max_length=30, verbose_name='name include')),
                ('text_1', models.TextField(verbose_name='text 1')),
                ('text_2', models.TextField(verbose_name='text 2')),
                ('text_3', models.TextField(verbose_name='text 3')),
                ('text_4', models.TextField(verbose_name='text 4')),
                ('text_5', models.TextField(verbose_name='text 5')),
                ('text_6', models.TextField(verbose_name='text 6')),
                ('text_7', models.TextField(verbose_name='text 7')),
                ('text_8', models.TextField(verbose_name='text 8')),
                ('text_9', models.TextField(verbose_name='text 9')),
                ('text_10', models.TextField(verbose_name='text 10')),
                ('text_11', models.TextField(verbose_name='text 11')),
            ],
        ),
    ]

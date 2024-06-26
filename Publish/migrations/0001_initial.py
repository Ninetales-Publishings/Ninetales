# Generated by Django 4.2.5 on 2024-03-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PubishedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookImage', models.ImageField(upload_to='')),
                ('BookName', models.CharField(default='book', max_length=40)),
                ('Writername', models.CharField(default='user', max_length=500)),
                ('ISBNNo', models.CharField(default='user', max_length=40)),
                ('Abstarct', models.TextField(default=None)),
                ('DOIDetail', models.CharField(default='user', max_length=40, null=True)),
            ],
        ),
    ]

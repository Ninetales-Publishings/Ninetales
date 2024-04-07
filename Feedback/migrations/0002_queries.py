# Generated by Django 4.2.5 on 2024-03-29 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='user', max_length=40)),
                ('email', models.EmailField(default=None, max_length=320)),
                ('query', models.CharField(default='Query', max_length=40)),
                ('subject', models.CharField(default='Subject', max_length=40)),
                ('message', models.TextField(default=None)),
                ('date_time', models.DateTimeField(null=True)),
            ],
        ),
    ]

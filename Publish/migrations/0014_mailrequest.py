# Generated by Django 5.0.3 on 2024-04-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publish', '0013_remove_pubishrequests_bookfile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(default='userMail', max_length=40)),
                ('Date_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
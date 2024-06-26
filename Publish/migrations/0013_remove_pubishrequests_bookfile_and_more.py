# Generated by Django 4.2.5 on 2024-04-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publish', '0012_pubishrequests_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pubishrequests',
            name='BookFile',
        ),
        migrations.AddField(
            model_name='pubishrequests',
            name='Address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='pubishrequests',
            name='AuthorProfile',
            field=models.FileField(default=None, null=True, upload_to='PublishRequests/AuthorProfile'),
        ),
        migrations.AddField(
            model_name='pubishrequests',
            name='Date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='pubishrequests',
            name='MainFile',
            field=models.FileField(default=None, null=True, upload_to='PublishRequests/MainFile'),
        ),
        migrations.AddField(
            model_name='pubishrequests',
            name='OtherFile',
            field=models.FileField(default=None, null=True, upload_to='PublishRequests/OtherFile'),
        ),
    ]

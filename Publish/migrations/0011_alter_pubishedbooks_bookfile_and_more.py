# Generated by Django 4.2.5 on 2024-03-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publish', '0010_rename_pubishrequestss_pubishrequests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubishedbooks',
            name='BookFile',
            field=models.FileField(default=None, null=True, upload_to='bookCover(ForPublishedBooks)/'),
        ),
        migrations.AlterField(
            model_name='pubishrequests',
            name='BookFile',
            field=models.FileField(default=None, null=True, upload_to='bookFile(ForPublishRequests)/'),
        ),
    ]

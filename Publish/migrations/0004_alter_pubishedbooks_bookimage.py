# Generated by Django 4.2.5 on 2024-03-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publish', '0003_alter_pubishedbooks_bookimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubishedbooks',
            name='BookImage',
            field=models.FileField(default=None, null=True, upload_to='bookCover/'),
        ),
    ]
# Generated by Django 4.2.5 on 2024-03-27 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Publish', '0007_rename_abstarct_pubishedbooks_abstract'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pubishedbooks',
            old_name='BookImage',
            new_name='BookFile',
        ),
    ]

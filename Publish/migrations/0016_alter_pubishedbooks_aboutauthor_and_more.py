# Generated by Django 4.2.5 on 2024-04-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publish', '0015_rename_abstract_pubishedbooks_aboutauthor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubishedbooks',
            name='AboutAuthor',
            field=models.TextField(default='aboutAuthor'),
        ),
        migrations.AlterField(
            model_name='pubishedbooks',
            name='AboutBook',
            field=models.TextField(default='aboutBook'),
        ),
    ]

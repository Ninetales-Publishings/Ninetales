# Generated by Django 4.2.5 on 2024-04-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0002_queries'),
    ]

    operations = [
        migrations.AddField(
            model_name='queries',
            name='mobileNo',
            field=models.CharField(default='user', max_length=20),
        ),
    ]

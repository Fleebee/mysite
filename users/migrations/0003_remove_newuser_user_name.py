# Generated by Django 5.0.3 on 2024-03-17 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newuser_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='user_name',
        ),
    ]

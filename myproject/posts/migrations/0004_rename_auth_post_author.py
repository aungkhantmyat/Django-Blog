# Generated by Django 5.0.6 on 2024-06-11 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_auth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auth',
            new_name='author',
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-09 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210209_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='user',
            new_name='profile',
        ),
    ]
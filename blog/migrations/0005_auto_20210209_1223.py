# Generated by Django 3.1.6 on 2021-02-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210209_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
# Generated by Django 3.1.6 on 2021-02-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210209_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='like',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
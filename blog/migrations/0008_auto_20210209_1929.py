# Generated by Django 3.1.6 on 2021-02-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210209_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

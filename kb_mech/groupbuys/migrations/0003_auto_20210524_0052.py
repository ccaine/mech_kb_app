# Generated by Django 3.2 on 2021-05-24 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groupbuys', '0002_auto_20210524_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupbuy',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='groupbuy',
            name='updated_at',
        ),
    ]

# Generated by Django 3.2 on 2021-05-24 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groupbuys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupbuy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupbuy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

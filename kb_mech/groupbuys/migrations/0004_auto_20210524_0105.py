# Generated by Django 3.2 on 2021-05-24 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groupbuys', '0003_auto_20210524_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupbuy',
            name='gb_end',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='groupbuy',
            name='gb_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupbuy',
            name='gb_start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

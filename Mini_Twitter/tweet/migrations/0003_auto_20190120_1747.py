# Generated by Django 2.0.10 on 2019-01-20 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20190120_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.BigIntegerField(default=0),
        ),
    ]

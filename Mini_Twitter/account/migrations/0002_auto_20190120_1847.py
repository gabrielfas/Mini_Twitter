# Generated by Django 2.0.10 on 2019-01-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='account.MyUser'),
        ),
    ]

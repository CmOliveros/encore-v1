# Generated by Django 3.2.4 on 2021-06-07 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210607_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='friends',
            field=models.JSONField(blank=True, default=list),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_appuser_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='associated_acts',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='talent',
            name='discography',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='talent',
            name='events',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='talent',
            name='fans',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='talent',
            name='genres',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='talent',
            name='members',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='events',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='venue',
            name='fans',
            field=models.JSONField(blank=True, default=list, editable=False),
        ),
    ]

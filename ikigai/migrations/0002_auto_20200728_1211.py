# Generated by Django 2.2.11 on 2020-07-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ikigai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='good',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='love',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='paid',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='worldNeed',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]

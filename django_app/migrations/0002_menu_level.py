# Generated by Django 4.2.6 on 2023-10-27 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
# Generated by Django 2.1.1 on 2018-09-01 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='image',
        ),
    ]

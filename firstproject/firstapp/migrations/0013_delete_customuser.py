# Generated by Django 5.0.4 on 2024-05-06 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_customuser_is_superuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_customuser_delete_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
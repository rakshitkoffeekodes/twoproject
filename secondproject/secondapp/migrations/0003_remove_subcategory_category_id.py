# Generated by Django 5.0.4 on 2024-04-24 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondapp', '0002_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category_id',
        ),
    ]

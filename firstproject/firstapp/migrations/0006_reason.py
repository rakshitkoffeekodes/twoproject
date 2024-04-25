# Generated by Django 5.0.4 on 2024-04-24 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_delete_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=1000)),
                ('sub_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.subcategory')),
            ],
        ),
    ]

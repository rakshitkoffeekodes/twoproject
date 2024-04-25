from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

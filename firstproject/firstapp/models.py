from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
# from .views import *


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    sub_category_id = models.IntegerField(primary_key=True, auto_created=True)
    sub_category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    reason = models.CharField(max_length=1000, null=True)
    accept = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name

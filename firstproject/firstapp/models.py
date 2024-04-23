from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class SubCategory(models.Model):
    sub_category_id = models.IntegerField(primary_key=True, auto_created=True)
    sub_category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def accept_reject_form(self):

        return print('-==-=-=-=-=-=')
        # if request.method == 'POST':
        #     option = request.POST.get('option')
        #     name = request.POST.get('name')
        #     print(option, name)
        #     return render(request, 'admin/change_list.html')
        #
        # else:
        #     return render(request, 'admin/change_list.html')

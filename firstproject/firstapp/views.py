from django.shortcuts import redirect, render
from .models import Category
from django.http import HttpRequest
import requests


def add_category(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        user_ip = request.META.get('REMOTE_ADDR')
        print('======>', user_ip)
        category = Category.objects.create(name=name, description=description)
        category.save()

        second_project_url = 'http://192.168.1.107:8001/category/'
        data = {'name': name, 'description': description}
        response = requests.post(second_project_url, data=data)
        return redirect('admin:index')

    return render(request, 'admin/change_list.html')


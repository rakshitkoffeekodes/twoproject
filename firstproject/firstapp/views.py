from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.decorators import api_view

from .models import Category, SubCategory
from django.http import HttpRequest
import requests

#
# def add_category(request: HttpRequest):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         user_ip = request.META.get('REMOTE_ADDR')
#         print('======>', user_ip)
#         category = Category.objects.create(name=name, description=description)
#         category.save()
#
#         second_project_url = 'http://192.168.1.107:8001/category/'
#         data = {'name': name, 'description': description}
#         response = requests.post(second_project_url, data=data)
#         return redirect('admin:index')
#
#     return render(request, 'admin/change_list.html')


def accept_reject_form(request):
    print('====')
    if request.method == 'POST':
        option = request.POST.get('option')
        name = request.POST.get('name')
        print(option, name)
        return render(request, 'admin/change_list.html')

    else:
        return render(request, 'admin/change_list.html')


# def open_popup(request):
#     return render(request, 'admin/change_list.html')

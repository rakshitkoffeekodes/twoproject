from django import forms
from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.decorators import api_view
from .models import *
import requests


# #
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

def accept_reject_form(request, pk):
    print('id============>', pk)
    print(request.method)
    print('=======>', request.GET.get('obj_id'))
    print('=======>', request.GET.get('name'))
    option = request.GET.get('option')
    name = request.GET.get('name')
    try:
        sub_category_data = SubCategory.objects.get(sub_category_id=pk)
        print('name', name, 'option', option)
        if option == 0:
            return redirect('admin:index')
        if name == '':
            return redirect('admin:index')
        if option == '1':
            print(name)
            url = name
            data = {'name': sub_category_data.sub_category_name, 'description': sub_category_data.description}
            response = requests.post(url, data=data)
            sub_category_data.accept = True
            sub_category_data.reason = '-'
            sub_category_data.save()
            return redirect('admin:index')

        elif option == '2':
            print(sub_category_data.sub_category_id)
            sub_category_data.reason = name
            sub_category_data.accept = False
            sub_category_data.save()
            return redirect('admin:index')
    except Exception as e:
        return redirect('admin:index')


def logout(request):
    return render(request, 'registration/logged_out.html')



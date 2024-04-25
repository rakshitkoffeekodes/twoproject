from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *


@api_view(['POST'])
def category_data(request):

    name = request.POST['name']
    description = request.POST['description']
    print(name, description)
    category = Category()
    category.name = name
    category.description = description
    category.save()
    return JsonResponse({'message': 'Category add successfully.'})


@api_view(['POST'])
def sub_category(request):
    sub_category_name = request.POST['name']
    description = request.POST['description']
    print(description, sub_category_name)
    add_sub_category = SubCategory()
    add_sub_category.sub_category_name = sub_category_name
    add_sub_category.description = description
    add_sub_category.save()
    return JsonResponse({'message': 'sub category data saved successfully.'})




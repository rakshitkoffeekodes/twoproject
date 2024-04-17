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



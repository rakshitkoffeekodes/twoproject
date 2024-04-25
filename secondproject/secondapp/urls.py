from django.urls import path
from .views import *

urlpatterns = [
    path('category/', category_data),
    path('sub-category/', sub_category)
]

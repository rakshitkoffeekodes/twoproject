from django.urls import path
from .views import *

urlpatterns = [
    path('save-category/', add_category, name='save_category'),
]

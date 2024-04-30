from django.urls import path
from. import views

urlpatterns = [
    # other URL patterns
    path('/accept_reject_form/<int:pk>/', views.accept_reject_form, name='accept_reject_form'),
    path('/logout/', views.logout, name='logout'),
]

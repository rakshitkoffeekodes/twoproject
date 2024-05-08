# from django.apps import AppConfig
from django.contrib.admin import apps


# class FirstappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'firstapp'

# This class is created to handle the custom admin site that has been created

class CustomAdminConfig(apps.SimpleAdminConfig):
    default_site = "firstapp.sites.AdminSite"
    name = 'firstapp'
    verbose_name = 'First App'

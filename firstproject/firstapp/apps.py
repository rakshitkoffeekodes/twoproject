# from django.apps import AppConfig
from django.contrib.admin import apps


# class FirstappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'firstapp'


class CustomAdminConfig(apps.SimpleAdminConfig):
    default_site = "firstapp.sites.AdminSite"
    name = 'firstapp'

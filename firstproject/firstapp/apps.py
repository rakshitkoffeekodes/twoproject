from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig as BaseAdminConfig


# class FirstappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'firstapp'


class CustomAdminConfig(BaseAdminConfig):
    default_site = "firstapp.sites.AdminSite"

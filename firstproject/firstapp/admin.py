# # from django.contrib import admin
# # from django.contrib.auth.hashers import make_password
# # from django.contrib.auth.models import User
# #
# #
# # class UserAdmin(admin.ModelAdmin):
# #     using = 'secondproject'
# #     def save_model(self, request, obj, form, change):
# #         obj.password = make_password(obj.password)
# #         obj.save()
# #         super().save_model(request, obj, form, change)
# #         if not change:
# #             # If this is a new user, create it in the 'secondproject' database
# #             User.objects.using('secondproject').create(
# #                 username=obj.username,
# #                 password=make_password(obj.password),
# #             )
# #
# #     def delete_model(self, request, obj):
# #         # Delete the user from the 'default' database
# #         User.objects.filter(username=obj.username).delete()
# #         # Delete the user from the 'secondproject' database
# #         User.objects.using('secondproject').filter(username=obj.username).delete()
# #
# #     def get_queryset(self, request):
# #         return super().get_queryset(request).using(self.using)
#
# # def formfield_for_foreignkey(self, db_field, request, **kwargs):
# #     return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
# #
# # def formfield_for_manytomany(self, db_field, request, **kwargs):
# #     return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
#
# # def delete_model(self, request, obj):
# #     obj.delete(using=self.using)
# #
# # def get_queryset(self, request):
# #     return super().get_queryset(request).using(self.using)
#
# # def formfield_for_foreignkey(self, db_field, request, **kwargs):
# #     return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
# #
# # def formfield_for_manytomany(self, db_field, request, **kwargs):
# #     return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
#
# #
# # admin.site.unregister(User)
# # admin.site.register(User, UserAdmin)
#
# #
# # from django.contrib import admin
# # from django.contrib.auth.models import User
# #
# #
# # class App1ModelAdmin(admin.ModelAdmin):
# #     using = 'secondproject'
# #
# #     def save_model(self, request, obj, form, change):
# #         obj.save(using=self.using)
# #
# #     def delete_model(self, request, obj):
# #         obj.delete(using=self.using)
# #
# #     def get_queryset(self, request):
# #         return super().get_queryset(request).using(self.using)
# #
# #     def formfield_for_foreignkey(self, db_field, request, **kwargs):
# #         return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)
# #
# #     def formfield_for_manytomany(self, db_field, request, **kwargs):
# #         return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)
# #
# #
# # # Register your models here.
# # admin.site.unregister(User)
# # admin.site.register(User, App1ModelAdmin)
#
#
# from django.contrib import admin
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
#
#
# class App1ModelAdmin(admin.ModelAdmin):
#     using = 'secondproject'
#
#     def save_model(self, request, obj, form, change):
#         obj.password = make_password(obj.password)
#         obj.save()
#         super().save_model(request, obj, form, change)
#         if not change:
#             User.objects.using('secondproject').create(
#                 username=obj.username,
#                 password=make_password(obj.password),
#             )
#
#     def delete_model(self, request, obj):
#         User.objects.using('secondproject').filter(username=obj.username).delete()
#         print('-------------->')
#         user = User.objects.filter(username=obj.username)
#         user.delete()
#
#     # def get_queryset(self, request):
#     #     return super().get_queryset(request).using(self.using)
#
#
# admin.site.unregister(User)
# admin.site.register(User, App1ModelAdmin)

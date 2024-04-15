# from django.contrib.auth.admin import UserAdmin
# from django.contrib import messages
# from django.core.management import call_command
# from rest_framework import status
#
#
# class CustomUserAdmin(UserAdmin):
#     def save_model(self, request, obj, form, change):
#         # Call the create_user API endpoint to save the user data in both MySQL databases
#         response = self.client.post('/api/create_auth/',
#                                     {'username': obj.username, 'password': obj.password, 'email': obj.email})
#
#         # Display a success message
#         if response.status_code == status.HTTP_201_CREATED:
#             messages.success(request, 'User created successfully.')
#
#         # Save the user in Django
#         super().save_model(request, obj, form, change)

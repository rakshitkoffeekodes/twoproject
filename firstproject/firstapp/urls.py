from django.urls import path
from . import views
from .admin import admin_site
from django.contrib.auth import views as auth_views

urlpatterns = [
    # other URL patterns
    path('myadmin/', admin_site.urls),
    path("admin/password_reset/", auth_views.PasswordResetView.as_view(), name="admin_password_reset", ),
    path("admin/password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done", ),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm", ),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
    path('/accept_reject_form/<int:pk>/', views.accept_reject_form, name='accept_reject_form'),
    path('/logout/', views.logout, name='logout'),
    path('/login/', views.login, name='login'),
]

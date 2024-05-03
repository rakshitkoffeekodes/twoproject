import uuid

import pyotp
import qrcode
import qrcode.image.svg
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from typing import Optional
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    sub_category_id = models.IntegerField(primary_key=True, auto_created=True)
    sub_category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    reason = models.CharField(max_length=1000, null=True)
    accept = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name


class UserTwoFactorAuthData(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='two_factor_auth_data',
        on_delete=models.CASCADE
    )

    otp_secret = models.CharField(max_length=255)
    session_identifier = models.UUIDField(blank=True, null=True)

    def generate_qr_code(self, name: Optional[str] = None, username: Optional[str] = None) -> str:
        totp = pyotp.TOTP(self.otp_secret)

        qr_uri = totp.provisioning_uri(
            name=name,
            issuer_name=username
        )

        image_factory = qrcode.image.svg.SvgPathImage
        qr_code_image = qrcode.make(
            qr_uri,
            image_factory=image_factory
        )

        # The result is going to be an HTML <svg> tag
        return qr_code_image.to_string().decode('utf_8')

    def validate_otp(self, otp: str) -> bool:
        totp = pyotp.TOTP(self.otp_secret)

        return totp.verify(otp)

    def rotate_session_identifier(self):
        self.session_identifier = uuid.uuid4()

        self.save(update_fields=["session_identifier"])


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models
#
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)
#
#
# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     full_name = models.CharField(max_length=255, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return self.email
#
#     def get_full_name(self):
#         return self.full_name
#
#     def get_short_name(self):
#         return self.email
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True

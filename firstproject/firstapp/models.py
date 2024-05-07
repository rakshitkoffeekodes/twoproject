import uuid
import pyotp
import qrcode
import qrcode.image.svg
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

    # this function is for generate qr code

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

    # this function is for validate otp

    def validate_otp(self, otp: str) -> bool:
        totp = pyotp.TOTP(self.otp_secret)

        return totp.verify(otp)

    # this function is for rotate session identifier

    def rotate_session_identifier(self):
        self.session_identifier = uuid.uuid4()

        self.save(update_fields=["session_identifier"])

    class Meta:
        verbose_name = 'User 2FA Data'

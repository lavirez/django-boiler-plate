from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group
from django.core.exceptions import ValidationError
from django.db.models.expressions import Exists, OuterRef

from src.apps.core.models import CreationModificationDateAbstractModel
from src.apps.core.utils.common import is_telephone_number_invalid


class UserManager(BaseUserManager["User"]):
    def create_user(
        self, phone_number, email=None, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        if email:
            email = UserManager.normalize_email(email)
        # Google OAuth2 backend send unnecessary username field
        extra_fields.pop("username", None)
        
        if is_telephone_number_invalid(phone_number):
            raise ValidationError("Phone number is not ok format.")

        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        user = self.create_user(
            phone_number, email, password, is_staff=True, is_superuser=True, **extra_fields
        )
        return user


class User(AbstractUser):
    phone_number = models.CharField(max_length=14, unique=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    national_id = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
    )
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    # user_type = models.CharField(max_length=16, choices=UserType)
    seller = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        return super().save()

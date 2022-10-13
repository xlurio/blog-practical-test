from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.services import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Model for the users data"""

    email: str = models.EmailField(
        verbose_name=_("email address"),
        max_length=255,
        unique=True,
        default="",
    )
    first_name: str = models.CharField(_("first name"), max_length=255)
    last_name: str = models.CharField(_("first name"), max_length=255)
    is_staff: bool = models.BooleanField(_("staff status"), default=False)
    is_active: bool = models.BooleanField(_("active"), default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    """Model for the categories data"""

    name: str = models.CharField(_("name"), max_length=255)


class News(models.Model):
    """Model for the news data"""

    title: str = models.CharField(_("title"), max_length=255, default="")
    content: str = models.TextField(_("content"), default="")
    category: Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=_("category"), null=True
    )
    author: User = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("author")
    )
    publication_date = models.DateTimeField(_("publication"), auto_now=True)

    @property
    def content_preview(self) -> str:
        """Property for getting the preview of the content"""
        return f"{self.content[:512]}..."

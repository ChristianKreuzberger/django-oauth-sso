from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """
    Extends the basic django user model with a longer first and last name
    """
    first_name = models.CharField(
        _("first name"),
        max_length=128,
        blank=True
    )

    last_name = models.CharField(
        _("last name"),
        max_length=128,
        blank=True
    )


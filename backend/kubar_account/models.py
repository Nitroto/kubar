from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class KubarUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254,
                              verbose_name=_("Email address"))

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

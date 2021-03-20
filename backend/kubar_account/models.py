from django.contrib.auth.models import AbstractUser
from django.db import models


class KubarUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=254,
                              verbose_name="email address")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

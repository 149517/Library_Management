from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    career = models.CharField("职业", max_length=24, default="")
    pic = models.CharField("头像", max_length=64, default="")

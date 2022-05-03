from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from backend import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
import backend.settings
from safedelete import SOFT_DELETE
from safedelete.managers import SafeDeleteManager
from safedelete.models import SafeDeleteModel
from .user import User

class CoachQuerySet(SafeDeleteQuerySet):
    pass



class Coach(SafeDeleteModel, User):
    



    objects = SafeDeleteManager.from_queryset(CoachQuerySet)()

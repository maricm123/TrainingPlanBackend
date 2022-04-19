from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from backend import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
import backend.settings

class MyUserManager(BaseUserManager):
  def create_user(self, email, username, password = None):
    if not email:
      raise ValueError("Users must have an email")
    if not username:
      raise ValueError("Users must have an username")

    user = self.model(
      email = self.normalize_email(email),
      username = username,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self, email, username, password):
    user = self.create_user(
      email= self.normalize_email(email),
      password = password,
      username = username,
    )
    user.is_admin = True
    user.is_client = True
    user.is_coach = True
    

    user.save(using = self._db)
    return user

class User(AbstractBaseUser):
  email = models.EmailField(verbose_name="email", max_length=60, unique=True)
  username = models.CharField(max_length=100, unique=True)
  is_client = models.BooleanField(default=False)
  is_coach = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  date_joined= models.DateTimeField(verbose_name='date_joined', auto_now_add=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']
  
  objects = MyUserManager()

  def __str__(self):
    return self.email

  @property
  def is_staff(self):
      return self.is_admin


  def has_perm(self, perm, obj = None):
    return self.is_admin
  
  def has_module_perms(self, app_label):
    return True
  
  @receiver(post_save, sender = backend.settings.base.AUTH_USER_MODEL)
  def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
      Token.objects.create(user = instance)
      


class Client(models.Model):
    client = models.OneToOneField(
      backend.settings.base.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)


    def __str__(self):
        return self.client.username

class Coach(models.Model):
    coach = models.OneToOneField(
        backend.settings.base.AUTH_USER_MODEL, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    biography = models.CharField(max_length=200, null=False)
    courses = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)

    sport_category = models.ForeignKey("trainingPlan.Category", on_delete = models.CASCADE, related_name='coach_category')
    plans = models.ForeignKey("trainingPlan.Plan", on_delete = models.CASCADE, related_name='coach_plans', null = True, blank = True)

    def __str__(self):
        return self.coach.username
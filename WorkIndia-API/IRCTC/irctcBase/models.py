from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# # Create your models here.
# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is needed')
        email = self.normalize_email(email)
        user = self.model(username = username, email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Super User must have is_staff as True'))
        return self.create_user(username, email, password, **extra_fields)
    
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return str(self.id)
    
class Train(models.Model):
    train_name = models.CharField(max_length=100, unique=True)
    source = models.CharField(max_length=50, unique=True)
    destination = models.CharField(max_length=50, unique=True)
    seat_capacity = models.IntegerField()
    arrival_time_at_source = models.CharField(max_length=8)
    arrival_time_at_destination = models.CharField(max_length=8)
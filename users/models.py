from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import AccountManager

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'instructor'),
        (3, 'student'),
    )
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    email = models.EmailField(('Email address'), unique=True)
    surname = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    dob = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # here you can list required fields for the createsuperuser command
    objects = AccountManager()

    class Meta:
        db_table = 'users'

    def get_full_name(self):
        return f"{self.first_name} {self.surname}"

    def __str__(self):
        return self.email


class Phone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='phones')
    number = models.CharField(max_length=20)
    otp = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.number

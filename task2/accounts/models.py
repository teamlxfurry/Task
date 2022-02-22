from datetime import datetime
import email
from turtle import mode
from django.db import models
from  django.contrib.auth.models import User
# from accounts.views import token
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)

    # created_at=models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.user.username
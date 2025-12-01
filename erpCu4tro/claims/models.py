from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client
User = get_user_model()
# Create your models here.
class Claim(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    file = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
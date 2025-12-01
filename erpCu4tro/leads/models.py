from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()
from clients.models import Client
# Create your models here.
class Lead(models.Model):
    email = models.EmailField()
    workflow_status = models.CharField(max_length=50)
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)
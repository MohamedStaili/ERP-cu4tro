from django.db import models
from django.contrib.auth import get_user_model
from clients.models import Client
User = get_user_model()
# Create your models here.
class Claim(models.Model):
    STATUS = [
        ("new", "Nouvelle"),
        ("in_review", "En cours d'étude"),
        ("approved", "Approuvée"),
        ("rejected", "Rejetée"),
        ("closed", "Clôturée"),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    file = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default="new"
        )
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
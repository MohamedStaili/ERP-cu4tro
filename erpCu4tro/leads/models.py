from django.db import models
from django.contrib.auth import get_user_model
from django.db import transaction
from django.contrib.auth.models import Group
User= get_user_model()
from clients.models import Client
# Create your models here.
class Lead(models.Model):
    WORKFLOW_STATUS = [
        ("new", "Nouveau"),
        ("assigned", "Assigné"),
        ("contacted", "Contacté"),
        ("qualified", "Qualifié"),
        ("converted", "Converti"),
        ("rejected", "Rejeté"),
        ("closed", "Fermé"),
    ]
    email = models.EmailField()
    workflow_status = models.CharField(max_length=50, choices=WORKFLOW_STATUS, default="new")
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)

    @transaction.atomic
    def convert_to_client(self, password, username):
        if self.client_id:
            return self.client
        user = User.objects.create_user(
            username=username,
            email=self.email,
            password=password,
        )

        try:
            client_group = Group.objects.get(name="client")
            user.groups.set([client_group]) 
        except Group.DoesNotExist:
            pass

        client = Client.objects.create(
            user=user,
            first_name=getattr(self, "first_name", ""),
            last_name=getattr(self, "last_name", ""),
            email=self.email,
            phone=getattr(self, "phone", ""),
        )
        self.client = client
        self.workflow_status = "converted"
        self.save()

        return client

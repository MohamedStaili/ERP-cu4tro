from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
User = get_user_model()
# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)     
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, through="ClientProduct", related_name="clients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class ClientProduct(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS= [
            ("requested", "Requested"),
            ("ordered", "Ordered"),
            ("delivered", "Delivered"),
            ("canceled", "Canceled")
        ]
    
    status = models.CharField(
        max_length=50,
        choices=STATUS,
        default="requested"
    )

    class Meta:
        unique_together = ("client", "product")

    def __str__(self):
        return f"{self.client} → {self.product} ({self.quantity})"
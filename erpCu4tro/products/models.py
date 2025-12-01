from django.db import models

# Create your models here.
class Product(models.Model):
    label = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    type = models.CharField(null=True)
    infos_dynamique = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.label
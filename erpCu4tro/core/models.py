from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
class Comment(models.Model):
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField() 
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content[:50]
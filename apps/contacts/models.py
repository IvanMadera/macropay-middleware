from django.db import models
from uuid import uuid4

# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    addressLines = models.CharField(max_length=255)

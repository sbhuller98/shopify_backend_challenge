from django.db import models
import uuid

# Create your models here.

class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=75)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

    

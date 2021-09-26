from django.db import models

# Create your models here.

class Images(models.Model):
    title = models.CharField(max_length=75)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/')

    

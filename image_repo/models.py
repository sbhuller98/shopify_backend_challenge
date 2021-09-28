from django.db import models
import uuid


# Create your models here.

class Images(models.Model):
    '''Defines Images object.'''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=75)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

    class Meta:
        '''Sets default ordering to display most recently uploaded images first.'''
        ordering = ['-date_added']

    

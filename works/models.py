from django.db import models

# Create your models here.
class works(models.Model):
    work = models.CharField(max_length=200)
    
    def __str__(self):
        return self.work
    

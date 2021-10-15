from django.db import models

# Create your models here.
class CarImage(models.Model):
    name = models.CharField(max_length = 100, null=True)
    car = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

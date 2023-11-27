from django.db import models

# Create your models here.

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    
    def __str__(self):  
        return self.first_name + " " + self.last_name  

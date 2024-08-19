from django.db import models

# Create your models here.
class user(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def _str__(self):
        return self.first_name + " "+ self.last_name
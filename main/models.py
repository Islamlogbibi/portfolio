from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length = 50)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name
    
class Login(models.Model):
    email = models.CharField(max_length = 50, null = False, blank = False)
    messege = models.TextField(max_length = 5000)
    

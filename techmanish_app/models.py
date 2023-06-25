from django.db import models

# Create your models here.
class user_login(models.Model):
    userid = models.CharField(max_length=50)
    password = models.IntegerField()
    
    def __str__(self) -> str:
        return self.userid
   
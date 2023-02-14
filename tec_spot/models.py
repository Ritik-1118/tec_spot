from django.db import models

# Create your models here.

class login(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.IntegerField()

    def __str__(self) -> str:
        return self.Name
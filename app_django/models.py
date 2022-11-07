from django.db import models

# Create your models here.

class Town(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=40)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

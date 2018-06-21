from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    description = models.TextField(blank=True)
    name = models.CharField(max_length=250)
    assignedTo = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    typePet = models.CharField(max_length=100)

    def __str__(self):
        return self.name
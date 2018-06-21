from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from pets.models import Pet

class Appointment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    dateAppointment = models.DateTimeField(default=datetime.now)
    place = models.CharField(max_length=250)
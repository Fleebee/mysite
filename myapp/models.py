from django.db import models
import uuid
from users.models import NewUser

# Create your models here.





class Colour(models.Model):
    name = models.CharField(max_length=50)
    paint_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    model_name = models.CharField(max_length=50)
    colour = models.ForeignKey(Colour, blank=True, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.SET_NULL)

    class Condition(models.TextChoices):
        NEW = "NEW", "New"
        USED = "USED", "Used"

    condition = models.CharField(max_length=4, choices=Condition.choices)

    def __str__(self):
        return f"{self.model_name} {self.colour} {self.brand} {self.condition}"


class Owner(models.Model):
    name = models.CharField(max_length=250)
    car = models.ForeignKey(Car, blank=True, null=True, on_delete=models.SET_NULL)
    owned_to = models.DateField()
    owned_from = models.DateField()

    def __str__(self):
        return f"{self.name}"

from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Car)
class Car(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Colour)
class Colour(admin.ModelAdmin):
    list_display = ["name"]

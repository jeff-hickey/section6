from django.contrib.auth.models import AbstractUser
from django.db import models


class Room(models.Model):
    label = models.CharField(max_length=64)
    room_number = models.PositiveIntegerField()
    room_price = models.DecimalField(max_digits=6, decimal_places=2)

    def serialize(self):
        return {
            "id": self.id,
            "label": self.label,
            "number": self.room_number,
            "price": self.room_price,
        }

    def __str__(self):
        return f"{self.label}"


class Hotel(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    hotel_name = models.CharField(max_length=64)
    about_hotel = models.TextField(max_length=10000)
    room_list = models.ManyToManyField(Room, related_name='hotel_rooms')

    def __str__(self):
        return f"{self.hotel_name}"


class Attraction(models.Model):
    label = models.CharField(max_length=64)
    stars = models.IntegerField(default=0)
    admission = models.DecimalField(max_digits=6, decimal_places=2)

    def serialize(self):
        return {
            "label": self.label,
            "stars": self.stars,
            "admission": self.admission
        }

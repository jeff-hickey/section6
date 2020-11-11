import json

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .views import _search

from .models import Hotel, Room


class HotelCase(TestCase):

    def setUp(self):
        pass

    def test_room_price(self):
        pass

    def test_hotel_rooms(self):
        pass

    def test_search(self):
        pass

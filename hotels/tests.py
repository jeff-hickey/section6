import json

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from .views import _search

from .models import Hotel, Room


class HotelCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='test')
        self.user.set_password('test')
        self.user.save()

        self.room_1 = Room.objects.create(label="King Suite", room_number=401,
                                          room_price=350)
        self.room_2 = Room.objects.create(label="Queen Suite", room_number=320,
                                          room_price=300)
        self.hotel = Hotel.objects.create(hotel_name="Super 8 ",
                                          about_hotel="Excellent Location")

        self.hotel.room_list.add(self.room_1)
        self.hotel_2 = Hotel.objects.create(hotel_name="Comfort Hotel",
                                            about_hotel="Reasonably Priced")
        self.hotel.room_list.add(self.room_2)

    def test_room_price(self):
        # Look at rooms & price data.
        response = self.client.get(reverse("prices"))
        self.assertEqual(response.status_code, 200)
        # Validate the two rooms created exist.
        data = json.loads(response.content)
        for room in data["rooms"]:
            assert room["label"] in ['King Suite', 'Queen Suite']
            assert room["number"] in [401, 320]

    def test_hotel_rooms(self):
        # User who is not logged in will be redirected.
        response = self.client.get(f"/rooms/{self.hotel.id}")
        self.assertEqual(response.status_code, 302)
        # Login the user.
        self.client.login(username='test', password='test')
        # User who is logged in can look at rooms.
        response = self.client.get(f"/rooms/{self.hotel.id}")
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        # Hotels with keyword in the title.
        search = _search("Comfort")
        # We created one matching hotel in setUp()
        self.assertTrue(len(search), 1)
        self.assertEquals(search[0].hotel_name, "Comfort Hotel")

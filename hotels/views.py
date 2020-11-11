import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Hotel, Room, Attraction


# Holds a list of hotel names.
# hotels = ['Super 8', 'Comfort Inn', 'Hilton Garden Inn', 'Marriott']


def index(request):
    """
    Default route that returns our hotel list.
    """
    hotels = Hotel.objects.all()
    return render(request, "hotels/index.html", {"hotels": hotels})


@csrf_exempt
def prices(request):
    """
    API endpoint to get a list of prices.
    :param request:
    :return: json formatted price for this room.
    """
    data = Room.objects.all()
    json_data = {
        "rooms": [room.serialize() for room in data]
    }
    return JsonResponse(json_data, safe=False)


@csrf_exempt
def attractions(request):
    """
    API endpoint to get a list of attractions.
    :param request:
    :return: json formatted list of attractions.
    """
    data = Attraction.objects.all()
    return JsonResponse([attraction.serialize() for attraction in data],
                        safe=False)


@login_required(login_url="login")
def find_rooms(request, hotel_id):
    """
    Looks up the room list for a hotel.
    :param request:
    :param hotel: hotel id
    :return: list of rooms
    """
    hotel = Hotel.objects.get(pk=hotel_id)
    rooms = Room.objects.filter(hotel_rooms=hotel_id)
    return render(request, "hotels/rooms.html",
                  {"hotel": hotel, "rooms": rooms})


@login_required(login_url="login")
def search(request, keyword):
    """
    Performs a search on the hotel list for keyword provided.
    This example gets the search param from our URL (see urls.py).
    :param request:
    :param keyword: input to search on
    :return: route to the search results page with hotels found.
    """
    results = _search(keyword)
    return render(request, "hotels/search.html", {"results": results})


def _search(keyword):
    """
    Searches hotel names for keyword and returns a list of hotels.
    :param keyword: search query.
    :return: list of hotels.
    """
    hotels = Hotel.objects.all()
    return [hotel for hotel in hotels if
            re.search(keyword, hotel.hotel_name, re.IGNORECASE)]


@login_required(login_url="login")
def search_form(request):
    """
    Performs a search on the hotel list for keyword provided.
    This example get the search param from a form (see index.html).
    :param request:
    :param keyword: input to search on
    :return: route to the search results page with hotels found.
    """
    if request.method == "POST":
        keyword = request.POST["keyword"]
        results = _search(keyword)
        return render(request, "hotels/search.html", {"results": results})
    # Anything other than a POST redirect to default.
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.POST:

        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct returning
        # User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page.
        if user:
            login(request, user)
            return render(request, "hotels/index.html", {
                "message": " You are Logged In."
            })
        # Otherwise, return login page again with new context
        else:
            return render(request, "hotels/index.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "hotels/login.html")


def logout_view(request):
    logout(request)
    return render(request, "hotels/login.html", {
        "message": "Successfully Logged Out"
    })

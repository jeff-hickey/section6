from django.contrib import admin
from hotels.models import Hotel, Room, Attraction


class HotelAdmin(admin.ModelAdmin):
    list_display = ("hotel_name", "create_date")


class RoomAdmin(admin.ModelAdmin):
    list_display = ("label", "room_number", "room_price")


class AttractionAdmin(admin.ModelAdmin):
    list_display = ("label", "admission", "stars")


class PriceAdmin(admin.ModelAdmin):
    list_display = ("room", "room_price")


# Register your models here.
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Attraction, AttractionAdmin)

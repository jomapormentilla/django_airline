from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights")

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
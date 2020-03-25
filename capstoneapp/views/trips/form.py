import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem
from capstoneapp.models import Trip
from capstoneapp.models import TripItem
from capstoneapp.models import Brand
from capstoneapp.models import Category
from capstoneapp.models import Customer

# from .trip_details import get_trip


def get_trip(trip_id):
    
    return Trip.objects.get(pk=trip_id)

@login_required
def trip_form(request):
    if request.method == 'GET':

        template = 'trips/form.html'

        

        return render(request, template)
      
@login_required
def trip_edit_form(request, trip_id):

    if request.method == 'GET':
        trip = get_trip(trip_id)


        template = 'trips/form.html'
        context = {
            'trip': trip,
        }


        return render(request, template, context)
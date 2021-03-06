import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem, Trip, TripItem



def trip_list(request):

    if request.method == 'GET':

        all_trips = Trip.objects.filter(user__user_id = request.user.id)

        trip_name = request.GET.get('trip_name', None)
        

        if trip_name is not None:
            all_trips = all_trips.filter(trip_name__contains=trip_name)

        template = 'trips/list.html'
        context = {
            'all_trips': all_trips
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_trip = Trip(
            trip_name = form_data['trip_name'],
            trip_date = form_data['trip_date'],
            user_id = request.user.id
        )
        
        new_trip.save()

        return redirect(reverse('capstoneapp:trips'))
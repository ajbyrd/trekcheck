import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem, Trip, TripItem



def trip_items_list(request, trip_id):

    
    form_data = request.POST

    new_trip_item = TripItem.objects.create(
    trip_id = trip_id,
    item_id = form_data['item']
    )

    new_trip_item.save()

    return redirect(reverse('capstoneapp:trip', args= (trip_id,)))
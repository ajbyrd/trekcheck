import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem, Category, Customer, Brand, Trip, TripItem
from django.db.models import Sum



def trip_item_weight_sum(trip_id):
    
    trip_item_weight_sum= TripItem.objects.filter(trip_id = trip_id).aggregate(Sum('item_id__weight'))['item_id__weight__sum']
    
    if (trip_item_weight_sum):
        round(trip_item_weight_sum,2)
    else:
        trip_item_weight_sum = 0

    return trip_item_weight_sum


@login_required
def trip_details(request, trip_id):
    if request.method == 'GET':
        all_items = InventoryItem.objects.filter(user__user_id = request.user.id)
        trip = Trip.objects.get(pk=trip_id)
        trip_items = TripItem.objects.filter(trip_id = trip_id)
        trip_weight = round(trip_item_weight_sum(trip_id), 2)
        template_name = 'trips/trip_detail.html'
        return render(request, template_name, {'trip': trip,
        'trip_items': trip_items, 'all_items': all_items, 'trip_weight': trip_weight})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a trip
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

                
            # # retrieve it first:
            trip_to_update = Trip.objects.get(pk=trip_id)

            # # Reassign a property's value

            trip_to_update.trip_name = form_data['trip_name']
            trip_to_update.trip_date = form_data['trip_date']            
                     


            # # Save the change to the db
            trip_to_update.save()

            return redirect(reverse('capstoneapp:trips'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
 
                
            trip = Trip.objects.get(pk=trip_id)
            trip.delete()

            return redirect(reverse('capstoneapp:trips'))
import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem, Category, Customer, Brand, Trip, TripItem

def get_trip_items(trip_id):


    trip_items = TripItem.objects.filter(trip_id = trip_id)
    print(trip_items)

    return trip_items

def get_inventory(request):

    all_items = InventoryItem.objects.filter(user__user_id = request.user.id)

    return all_items

def get_trip(trip_id):

    return Trip.objects.get(pk=trip_id)

def create_trip_item(request, trip_id):

    form_data = request.POST

    new_trip_item = TripItem.objects.create(
    trip_id = trip_id,
    item_id = form_data['item']
    )

    new_trip_item.save()

    return redirect(reverse('capstoneapp:trip'))



@login_required
def trip_details(request, trip_id):
    if request.method == 'GET':
        all_items = get_inventory(request)
        trip = get_trip(trip_id)
        trip_items = get_trip_items(trip_id)
        template_name = 'trips/trip_detail.html'
        return render(request, template_name, {'trip': trip,
        'trip_items': trip_items, 'all_items': all_items})

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
            # trip_to_update.user = request.user.Customer.id           


            # # Save the change to the db
            trip_to_update.save()

            return redirect(reverse('capstoneapp:trips'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #         DELETE FROM capstoneapp_book
            #         WHERE id = ?
            #     """, (book_id,))
                
            trip = Trip.objects.get(pk=trip_id)
            trip.delete()

            return redirect(reverse('capstoneapp:trips'))
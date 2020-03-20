import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem
from capstoneapp.models import Trip
from capstoneapp.models import TripItem
from capstoneapp.models import Brand
from capstoneapp.models import Category
from capstoneapp.models import Customer
from ..connection import Connection
from .trip_details import get_trip

# def get_categories():
#     # with sqlite3.connect(Connection.db_path) as conn:
#     #     conn.row_factory = sqlite3.Row
#     #     db_cursor = conn.cursor()

#     #     db_cursor.execute("""
#     #     select
#     #         cc.id,
#     #         cc.category_name,
            
#     #     from capstoneapp_category cc
#     #     """)

#     #     return db_cursor.fetchall()

#     all_categories = Category.objects.all()
        
# def get_brands():
#     # with sqlite3.connect(Connection.db_path) as conn:
#     #     conn.row_factory = sqlite3.Row
#     #     db_cursor = conn.cursor()

#     #     db_cursor.execute("""
#     #     select
#     #         cb.id,
#     #         cb.brand_name,
            
#     #     from capstoneapp_brand cb
#     #     """)

#     #     return db_cursor.fetchall()

#     all_brands = Brand.objects.all()

def get_trip(trip_id):
    
    return Trip.objects.get(pk=trip_id)

@login_required
def trip_form(request):
    if request.method == 'GET':

        template = 'trips/form.html'
        context = {
            
        }

        return render(request, template, context)
      
@login_required
def trip_edit_form(request, trip_id):

    if request.method == 'GET':
        trip = get_trip(trip_id)


        template = 'trips/form.html'
        context = {
            'trip': trip,
        }


        return render(request, template, context)
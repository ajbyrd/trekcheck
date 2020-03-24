import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem
from capstoneapp.models import Trip
from capstoneapp.models import TripItem
from capstoneapp.models import Brand
from capstoneapp.models import Category
from capstoneapp.models import Customer


@login_required
def brand_form(request):
    if request.method == 'GET':

        template = 'brands/form.html'

        return render(request, template)
      

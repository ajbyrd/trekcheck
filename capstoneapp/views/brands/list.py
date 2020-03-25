import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem, Customer, Category, Brand






def brand_list(request):

    if request.method == 'GET':

        all_brands = Brand.objects.all()

        template = 'brand/form.html'
        context = {
            'all_brands': all_brands
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_brand = Brand.objects.create(
            brand_name = form_data['brand_name']
        )

        new_brand.save()

        return redirect(reverse('capstoneapp:inventoryform'))
import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem, Customer






def inventory_list(request):

    if request.method == 'GET':

        all_items = InventoryItem.objects.all()

        model_name = request.GET.get('model_name', None)


        if model_name is not None:
            all_items = all_items.filter(model_name__contains=model_name)

        template = 'inventory/list.html'
        context = {
            'all_items': all_items
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_item = InventoryItem(
            model_name = form_data['model_name'],
            weight = form_data['weight'],
            description = form_data['description'],
            image_path = form_data['image_path'],
            user = request.user.Customer.id,
            category = form_data['category_name'],
            brand = form_data['brand_name']
        )


        print(new_item.Customer.user.username)
        new_item.save()
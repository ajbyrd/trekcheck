import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem, Customer, Category, Brand






def inventory_list(request):

    if request.method == 'GET':

        all_items = InventoryItem.objects.filter(user__user_id = request.user.id)


        template = 'inventory/list.html'
        context = {
            'all_items': all_items
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST


        new_item = InventoryItem.objects.create(
            model_name = form_data['model_name'],
            weight = form_data['weight'],
            description = form_data['description'],
            # image_path = form_data['image_path'],
            user_id = request.user.id,
            category_id = form_data['category_name'],
            brand_id = form_data['brand_name']
        )

        new_item.save()

        return redirect(reverse('capstoneapp:inventory'))
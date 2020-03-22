import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem, Category, Customer, Brand
# from capstoneapp.models import model_factory



def get_item(item_id):

    return InventoryItem.objects.get(pk=item_id)


@login_required
def item_details(request, item_id):
    if request.method == 'GET':
        item = get_item(item_id)
        template_name = 'inventory/item_detail.html'
        return render(request, template_name, {'item': item})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            # # retrieve it first:
            item_to_update = InventoryItem.objects.get(pk=item_id)

            # # Reassign a property's value
            item_to_update.model_name = form_data['model_name']
            item_to_update.weight = form_data['weight']
            item_to_update.description = form_data['description']
            item_to_update.image_path = form_data['image_path']
            item_to_update.brand = form_data['brand']
            item_to_update.category = form_data['category']            
            item_to_update.user = request.user.id           


            # # Save the change to the db
            item_to_update.save()

            return redirect(reverse('capstoneapp:inventory'))

        # Check if this POST is for deleting a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

                
            item = InventoryItem.objects.get(pk=item_id)
            item.delete()

            return redirect(reverse('capstoneapp:inventory'))
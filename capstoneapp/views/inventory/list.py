import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem, Customer, Category, Brand






def inventory_list(request):

    if request.method == 'GET':

        all_items = InventoryItem.objects.filter(user__user_id = request.user.id)

        # model_name = request.GET.get('model_name', None)


        # if model_name is not None:
        #     all_items = all_items.filter(model_name__contains=model_name)

        template = 'inventory/list.html'
        context = {
            'all_items': all_items
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # new_category = Category.objects.create(
        #     category_name = form_data['category_name']
        # )

        # new_brand = Brand.objects.create(
        
        #    brand_name = form_data['brand_name']

        # )

        # new_category.save()

        # new_brand.save()

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
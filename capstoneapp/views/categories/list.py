import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem, Customer, Category, Brand






def category_list(request):

    if request.method == 'GET':

        all_categories = Category.objects.all()

        template = 'category/form.html'
        context = {
            'all_categories': all_categories
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_category = Category.objects.create(
            category_name = form_data['category_name']
        )

        new_category.save()

        return redirect(reverse('capstoneapp:inventoryform'))
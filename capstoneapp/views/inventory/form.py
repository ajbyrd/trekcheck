import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem
from capstoneapp.models import Brand
from capstoneapp.models import Category
from capstoneapp.models import Customer

from .item_details import get_item


def get_categories():
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = sqlite3.Row
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     select
    #         cc.id,
    #         cc.category_name,
            
    #     from capstoneapp_category cc
    #     """)

    #     return db_cursor.fetchall()

    all_categories = Category.objects.all()
        
def get_brands():
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = sqlite3.Row
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     select
    #         cb.id,
    #         cb.brand_name,
            
    #     from capstoneapp_brand cb
    #     """)

    #     return db_cursor.fetchall()

    all_brands = Brand.objects.all()

def get_item(item_id):
    
    return InventoryItem.objects.get(pk=item_id)

@login_required
def inventory_form(request):
    
    print(request.user.id)
    if request.method == 'GET':
        categories = get_categories()
        brands = get_brands()
        template = 'inventory/form.html'
        context = {
            'all_categories': categories,
            'all_brands': brands,
        }

        return render(request, template, context)
      
@login_required
def inventory_edit_form(request, item_id):

    if request.method == 'GET':
        item = get_item(item_id)
        categories = get_categories()
        brands = get_brands()

        template = 'inventory/form.html'
        context = {
            'item': item,
            'all_categories': categories,
            'all_brands': brands,
        }

        return render(request, template, context)
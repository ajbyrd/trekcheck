import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from capstoneapp.models import InventoryItem, Category, Customer, Brand
# from capstoneapp.models import model_factory
from ..connection import Connection


def get_item(item_id):
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Book)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         b.id,
    #         b.title,
    #         b.isbn,
    #         b.author,
    #         b.year,
    #         b.librarian_id,
    #         b.location_id
    #     FROM capstoneapp_book b
    #     WHERE b.id = ?
    #     """, (book_id,))

    #     return db_cursor.fetchone()
      
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
            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #     UPDATE capstoneapp_book
            #     SET title = ?,
            #         author = ?,
            #         isbn = ?,
            #         year = ?,
            #         location_id = ?
            #     WHERE id = ?
            #     """,
            #     (
            #         form_data['title'], form_data['author'],
            #         form_data['isbn'], form_data['year_published'],
            #         form_data["location"], book_id,
            #     ))
                
            # # retrieve it first:
            item_to_update = InventoryItem.objects.get(pk=item_id)

            # # Reassign a property's value
            item_to_update.model_name = form_data['model_name']
            item_to_update.weight = form_data['weight']
            item_to_update.description = form_data['description']
            item_to_update.image_path = form_data['image_path']
            item_to_update.brand = form_data['brand']
            item_to_update.category = form_data['category']            
            item_to_update.user = request.user.Customer.id           


            # # Save the change to the db
            item_to_update.save()

            return redirect(reverse('capstoneapp:inventory'))

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
                
            item = InventoryItem.objects.get(pk=item_id)
            item.delete()

            return redirect(reverse('capstoneapp:inventory'))
import sqlite3
from django.shortcuts import redirect, render, reverse
from capstoneapp.models import InventoryItem






def inventory_list(request):

    if request.method == 'GET':
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     select
        #         b.id,
        #         b.title,
        #         b.isbn,
        #         b.author,
        #         b.year,
        #         b.librarian_id,
        #         b.location_id
        #     from libraryapp_book b
        #     """)

        #     all_books = []
        #     dataset = db_cursor.fetchall()

        #     for row in dataset:
        #         book = Book()
        #         book.id = row['id']
        #         book.title = row['title']
        #         book.isbn = row['isbn']
        #         book.author = row['author']
        #         book.year = row['year']
        #         book.librarian_id = row['librarian_id']
        #         book.location_id = row['location_id']

        #         all_books.append(book)
        all_items = InventoryItem.objects.all()

        model_name = request.GET.get('model_name', None)
        # title = request.GET['title']

        if model_name is not None:
            all_items = all_items.filter(model_name__contains=model_name)

        template = 'inventory/list.html'
        context = {
            'all_items': all_items
        }

        return render(request, template, context)
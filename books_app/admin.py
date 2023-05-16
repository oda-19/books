from django.contrib import admin

from books_app.models import Authors, Books, Publishers

admin.site.register(Authors)
admin.site.register(Publishers)
admin.site.register(Books)

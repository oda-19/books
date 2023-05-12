from django.contrib import admin

from books_app.models import Authors, PublishingHouse, Books

admin.site.register(Authors)
admin.site.register(PublishingHouse)
admin.site.register(Books)

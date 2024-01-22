from django.contrib import admin

from bookshop.models import Book, Store, Publisher, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "rating", "price", ]
    date_hierarchy = "pubdate"

class BoookInline(admin.StackedInline):
    model = Book
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]
    inlines = [BoookInline,]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_active', 'address']

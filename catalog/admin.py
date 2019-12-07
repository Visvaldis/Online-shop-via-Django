from django.contrib import admin
from .models import Category, Product


# Register your models here.

# Define the admin class
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')


# Register the admin class with the associated model
admin.site.register(Product, ProductAdmin)


# Register the Admin classes for Category using the decorator
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]

    prepopulated_field = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'brand',
        'slug',
        'price',
        'in_stock',
        'created_at',
        'updated_at',
    ]

    list_filter = [
        'in_stock',
        'is_active',
    ]

    list_editable = [
        'price',
        'in_stock',
    ]

    prepopulated_field = {'slug': ('title',)}

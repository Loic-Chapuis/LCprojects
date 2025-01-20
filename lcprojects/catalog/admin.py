from django.contrib import admin
from .models import Product, Category, ProductImage, ProductAttribute

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'status', 'stock_quantity', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ProductImage)
admin.site.register(ProductAttribute)
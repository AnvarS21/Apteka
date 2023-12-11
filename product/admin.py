from django.contrib import admin

from product.models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_products')

    def get_products(self, obj):
        return [x for x in obj.products.all()]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'get_desc',
        'image',
        'price',
        'group',
        'quantity',
    )
    list_display_links = ('title', 'get_desc')
    search_fields = ('title', 'desc')

    def get_desc(self, obj):
        return obj.desc[:50] + '...'
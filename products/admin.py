from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from products.models import Product, Group


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_desc', 'image', 'price', 'quantity', 'drug_group')
    list_display_links = ('title', 'image')
    search_fields = ('id', 'title', 'desc', 'image', 'price', 'quantity', 'drug_group')

    def get_desc(self, obj):

        return obj.desc[:25] + '...'

admin.site.register(Group)



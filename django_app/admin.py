from django.contrib import admin

from django_app.models import Menu


@admin.register(Menu)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('menu_item_name', 'menu_item_reference', 'parent_menu_item')
    list_filter = ('menu_item_name',)
    search_fields = ('menu_item_name',)

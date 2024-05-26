from django.contrib import admin
from .models import Client, Product, Order, OrderItem


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'date_added']
    list_filter = ['price', 'quantity']
    search_fields = ['name']
    search_help_text = 'Поиск по названию'
    actions = [reset_quantity]
    readonly_fields = ['date_added']


admin.site.register(Product, ProductAdmin)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'registration_date')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'date_placed')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')

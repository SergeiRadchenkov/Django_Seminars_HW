from django.contrib import admin
from .models import Client, Product, Order, OrderProduct


class AdminClient(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')
    list_filter = ('registration_date', )
    search_fields = ('name', 'phone_number')
    fieldsets = [
        ['Данные клиента',
        {
            'fields': ('name', 'address' ),
        }],
        ['Контакты клиента',
         {
             'fields': ('email', 'phone_number', ),
         }]
    ]


admin.site.register(Client, AdminClient)
admin.site.register(Product)
admin.site.register(Order)

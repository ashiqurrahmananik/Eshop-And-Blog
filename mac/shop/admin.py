from django.contrib import admin

# Register your models here.

from .models import product, contact, orders

admin.site.register(product)

admin.site.register(contact)

admin.site.register(orders)
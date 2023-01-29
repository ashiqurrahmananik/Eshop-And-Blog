from django.contrib import admin

# Register your models here.

from .models import product, contact

admin.site.register(product)

admin.site.register(contact)
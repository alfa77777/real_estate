from django.contrib import admin

from .models import House, Category, Owner, Country

admin.site.register(House)
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(Country)

from django.contrib import admin
from .models import Product, Tag, UserProfile

admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(UserProfile)
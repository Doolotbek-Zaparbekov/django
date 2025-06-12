from django.contrib import admin
from. import models
from .models import NewsBook


admin.site.register(models.Book)
admin.site.register(models.Reviews)
@admin.register(NewsBook)
class NewsBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
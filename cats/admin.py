from django.contrib import admin
from .models import Cats


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Cats, CatAdmin)

from django.contrib import admin

from api.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
admin.site.register(Pet, PetAdmin)

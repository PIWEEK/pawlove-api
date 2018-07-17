from django.contrib import admin

from api.models import (Adopter, Association, Manager,
                        Pet, PetImage)



class ImageInline(admin.TabularInline):
    model = PetImage

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'race')
    inlines = [
        ImageInline,
    ]
admin.site.register(Pet, PetAdmin)

class AdopterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Adopter, AdopterAdmin)

class ManagerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Manager, ManagerAdmin)

class AssociationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Association, AssociationAdmin)

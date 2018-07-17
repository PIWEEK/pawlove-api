from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.forms import SelectMultiple
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm,
    UserChangeForm as DjangoUserChangeForm,
    UsernameField
)

from api.models import (Association, Pet, PetImage, User, Editor, Adopter)


class ImageInline(admin.TabularInline):
    model = PetImage


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'race')
    inlines = [
        ImageInline,
    ]


@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Editores", is_stacked=False)},
    }
    fieldsets = (
        (None, {"fields": ("name", )}),
        ("Información general", {"fields": ("name", "location", "description")}),
        ("Contacto", {"fields": ("website", "twitter", "email")}),
        ("Editores", {"fields": ("editors",)})
    )

    #def formfield_for_manytomany(self, db_field, request, **kwargs):
    #    if db_field.name == "editors":
    #        if '/change' in request.path:
    #            association_id = request.path.split("/")[4]
    #            kwargs["queryset"] = Editor.objects.filter(associations__in=[association_id])
    #    return super().formfield_for_manytomany(db_field, request, **kwargs)


class UserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}


class UserChangeForm(DjangoUserChangeForm):
    class Meta:
        model = User
        fields = "__all__"
        field_classes = {"username": UsernameField}


@admin.register(Editor)
class EditorAdmin(DjangoUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        super().save_model(request, obj, form, change)


@admin.register(Adopter)
class AdopterAdmin(DjangoUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    def save_model(self, request, obj, form, change):
        obj.is_staff = False
        super().save_model(request, obj, form, change)

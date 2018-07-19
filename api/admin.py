from django.contrib import admin
from django.contrib.auth.models import User, Permission
from django.db import models
from django.forms import SelectMultiple, EmailField
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm,
    UserChangeForm as DjangoUserChangeForm,
    UsernameField
)

from api.models import (Association, Pet, PetImage, User, Editor, Adopter, Tag, Answer, Question)


class UserCreationForm(DjangoUserCreationForm):

    class Meta:
        model = User
        fields = '__all__'


class UserChangeForm(DjangoUserChangeForm):

    class Meta:
        model = User
        fields = "__all__"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ImageInline(admin.TabularInline):
    model = PetImage


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    queryset = Pet.objects.all()
    list_display = ('name', 'race')
    exclude = ('followers',)
    readonly_fields = ('association',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Etiquetas", is_stacked=False)},
    }
    inlines = [
        ImageInline,
    ]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return self.queryset

        associations = Editor.objects.get(id=request.user.id).associations.all()
        pets = Pet.objects.filter(association__in=associations).distinct()
        return pets


@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    queryset = Association.objects.all()
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Editores", is_stacked=False)},
    }
    fieldsets = (
        ("Información general", {"fields": ("name", "location", "description", "logo")}),
        ("Contacto", {"fields": ("website", "twitter", "email")}),
        ("Editores", {"fields": ("editors",)})
    )

    def get_queryset(self, request):
        if request.user.is_superuser:
            return self.queryset

        associations = Editor.objects.get(id=request.user.id).associations.all()
        return associations


class AssociationInline(admin.TabularInline):
    model = Association


@admin.register(Editor)
class EditorAdmin(DjangoUserAdmin):
    queryset = Editor.objects.all()
    form = UserChangeForm
    add_form = UserCreationForm

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()

        return ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",
                "last_login", "date_joined")

    def get_queryset(self, request):
        if request.user.is_superuser:
            return self.queryset

        associations = Editor.objects.get(id=request.user.id).associations.all()
        editors = Editor.objects.filter(associations__in=associations).distinct()
        return editors


    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        super().save_model(request, obj, form, change)
        permissions = []
        perm_names = ['Can change association', 'Can add Editor', 'Can change Editor', 'Can delete Editor',
                 'Can add pet', 'Can change pet', 'Can delete pet', 'Can add pet image',
                 'Can change pet image', 'Can delete pet image']
        for perm_name in perm_names:
           perm = Permission.objects.get(name=perm_name)
           permissions.append(perm)

        obj.user_permissions.set(permissions)


@admin.register(Adopter)
class AdopterAdmin(DjangoUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    def save_model(self, request, obj, form, change):
        obj.is_staff = False
        super().save_model(request, obj, form, change)


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

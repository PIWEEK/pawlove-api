from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User


class User(AbstractUser):
    pass


class Editor(User):

    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural = 'Editors'


class Adopter(User):

    class Meta:
        verbose_name = 'Adopter'
        verbose_name_plural = 'Adopters'


class Pet(models.Model):
    SEX_CHOICES = (
        ('M', 'Macho'),
        ('H', 'Hembra'),
    )
    SPECIE_CHOICES = (
        ('P', 'Perro'),
        ('G', 'Gato'),
    )
    SIZE_CHOICES = (
        ('P', 'Pequeño'),
        ('M', 'Mediano'),
        ('G', 'Grande'),
    )
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    specie = models.CharField(max_length=1, choices=SPECIE_CHOICES)
    race = models.CharField(max_length=100)
    birth_date = models.DateField()
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    personality_1 = models.TextField(blank=True, null=True)
    personality_2 = models.TextField(blank=True, null=True)
    personality_joke = models.TextField(blank=True, null=True)
    association = models.ForeignKey('Association', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    @property
    def age(self):
        now = datetime.datetime.now
        dob = self.birth_date
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return age


class PetImage(models.Model):
    pet = models.ForeignKey(Pet, related_name='images',
            on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads',
            blank=False, null=False)


PROVINCE_CHOICES = (
    ("Araba", "Araba"), ("Albacete", "Albacete"), ("Alicante", "Alicante"), ("Almería", "Almería"),
    ("Asturias", "Asturias"), ("Ávila", "Ávila"), ("Badajoz", "Badajoz"), ("Barcelona", "Barcelona"),
    ("Bizkaia", "Bizkaia"), ("Burgos", "Burgos"), ("Cáceres", "Cáceres"), ("Cádiz", "Cádiz"),
    ("Cantabria", "Cantabria"), ("Castellón", "Castellón"), ("Ceuta", "Ceuta"), ("Ciudad", "Ciudad"),
    ("Córdoba", "Córdoba"), ("Cuenca", "Cuenca"), ("Girona", "Girona"), ("Granada", "Granada"),
    ("Guadalajara", "Guadalajara"), ("Gipuzkoa", "Gipuzkoa"), ("Huelva", "Huelva"), ("Huesca", "Huesca"),
    ("Islas Baleares", "Islas Baleares"), ("Jaén", "Jaén"), ("La Coruña", "La Coruña"), ("La Rioja", "La Rioja"),
    ("Las Palmas", "Las Palmas"), ("León", "León"), ("Lleida", "Lleida"), ("Lugo", "Lugo"), ("Madrid", "Madrid"),
    ("Málaga", "Málaga"), ("Melilla", "Melilla"), ("Murcia", "Murcia"), ("Navarra", "Navarra"),
    ("Ourense", "Ourense"), ("Palencia", "Palencia"), ("Pontevedra", "Pontevedra"), ("Salamanca", "Salamanca"),
    ("Segovia", "Segovia"), ("Sevilla", "Sevilla"), ("Soria", "Soria"), ("Tarragona", "Tarragona"),
    ("Tenerife", "Tenerife"), ("Teruel", "Teruel"), ("Toledo", "Toledo"), ("Valencia", "Valencia"),
    ("Valladolid", "Valladolid"), ("Zamora", "Zamora"), ("Zaragoza", "Zaragoza"),
)


class Association(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=PROVINCE_CHOICES)
    website = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    editors = models.ManyToManyField('Editor', related_name='associations')

    def __str__(self):
        return self.name


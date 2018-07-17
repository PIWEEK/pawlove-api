from django.db import models

class Pet(models.Model):
    SEX_CHOICES = (
        ('M', 'Mujer'),
        ('H', 'Hombre'),
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


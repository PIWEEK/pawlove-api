from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

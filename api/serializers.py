from rest_framework import serializers
from api.models import Pet

class PetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pet


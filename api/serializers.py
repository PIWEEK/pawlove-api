from rest_framework import serializers
from api.models import Pet, Association, Editor


class EditorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Editor
        fields = '__all__'


class AssociationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Association
        fields = '__all__'



class PetSerializer(serializers.HyperlinkedModelSerializer):
    association = AssociationSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'



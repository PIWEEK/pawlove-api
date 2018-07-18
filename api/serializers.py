from rest_framework import serializers
from api.models import Pet, Association, Editor, PetImage


class AssociationSerializer(serializers.HyperlinkedModelSerializer):
    pets = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pet-detail'
    )

    class Meta:
        model = Association
        exclude = ('editors',)

class SummaryAssociationSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Association
        exclude = ('editors',)

class PetImageSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = PetImage
        fields = '__all__'

class PetSerializer(serializers.HyperlinkedModelSerializer):
    association = SummaryAssociationSerializer(read_only=True)    
    #images = PetImageSerializer(read_only=True, many=True)

    class Meta:
        model = Pet
        fields = '__all__'




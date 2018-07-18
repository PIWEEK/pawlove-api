from rest_framework import serializers
from api.models import Pet, Association, Editor, PetImage, Tag


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


class PetImageSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        """Convert `dict` to element."""
        ret = super().to_representation(instance)
        ret = ret['image']
        return ret

    class Meta:
        model = PetImage
        fields = ('image',)


class TagSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = ret['name']
        return ret

    class Meta:
        model = Tag
        fields = ('name',)


class PetSerializer(serializers.HyperlinkedModelSerializer):
    association = SummaryAssociationSerializer(read_only=True)
    images = PetImageSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Pet
        fields = '__all__'




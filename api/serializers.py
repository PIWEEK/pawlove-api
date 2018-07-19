from rest_framework import serializers
from api.models import Pet, Association, Editor, PetImage, Tag, Question, Answer, Adopter


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


class AdopterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Adopter
        fields = ('first_name', 'last_name', 'url')


class SummaryPetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pet
        fields = ('url', 'name')


class CompleteAdopterSerializer(serializers.HyperlinkedModelSerializer):
    following = SummaryPetSerializer(read_only=True, many=True)

    class Meta:
        model = Adopter
        fields = ('first_name', 'last_name', 'url', 'following')


class PetSerializer(serializers.HyperlinkedModelSerializer):
    association = SummaryAssociationSerializer(read_only=True)
    images = PetImageSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)
    followers = AdopterSerializer(read_only=True, many=True)
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        return obj.age

    class Meta:
        model = Pet
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        exclude = ('tag', 'question')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = '__all__'

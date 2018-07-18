from rest_framework import viewsets
from api.models import Pet, Association, Editor, Question
from api.serializers import PetSerializer, AssociationSerializer, QuestionSerializer


class PetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class AssociationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

from rest_framework import viewsets
from api.models import Pet, Association, Editor
from api.serializers import PetSerializer, AssociationSerializer, EditorSerializer


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


class EditorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Editor.objects.all()
    serializer_class = EditorSerializer

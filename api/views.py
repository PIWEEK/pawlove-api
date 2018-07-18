from rest_framework import viewsets

from api.models import Pet, Association, Editor, Question, Answer, Tag
from api.serializers import PetSerializer, AssociationSerializer, QuestionSerializer


class PetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = self.queryset

        if 'answers' in self.request.query_params:
            answers = self.request.query_params['answers'].split(',')
            for answer_id in answers:
                answer = Answer.objects.filter(id=answer_id).first()
                if answer and answer.tag:
                    return [answer.tag.pets.all().order_by('?').first()]
            return [queryset.order_by('?').first()]

        return queryset


class AssociationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

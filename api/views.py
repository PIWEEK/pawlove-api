from django.db.models import Count
from rest_framework import viewsets

from api.models import Pet, Association, Editor, Question, Answer, Tag, Adopter
from api.serializers import PetSerializer, AssociationSerializer, QuestionSerializer, CompleteAdopterSerializer


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
            tags = []
            species = []
            for answer_id in answers:
                answer = Answer.objects.filter(id=answer_id).first()
                if answer:
                    if answer.tag:
                        tags.append(answer.tag.id)
                    if answer.specie:
                        species.append(answer.specie)

            species = list(set(species))
            if len(species) == 1: # las respuestas indican "PERRO XOR GATO"
                queryset = queryset.filter(specie=species[0])

            tags_ids = list(set(tags))
            if len(tags_ids) != 0:
                queryset = queryset.filter(tags__in=tags_ids).annotate(num_tags=Count('id')).order_by('-num_tags')

            if len(queryset) > 0:
                return [queryset.first()]

            return [self.queryset.order_by('?').first()]

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


class AdopterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Adopter.objects.all()
    serializer_class = CompleteAdopterSerializer

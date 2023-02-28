import graphene
from graphene_django import DjangoObjectType

from .models import Auto


class AutoType(DjangoObjectType):
    class Meta:
        model = Auto


class Query(graphene.ObjectType):
    autos = graphene.List(AutoType)

    def resolve_autos(self, info, **kwargs):
        return Auto.objects.all()

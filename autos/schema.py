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

# ...code
#1
class CreateAuto(graphene.Mutation):
    id = graphene.Int()
    modelo = graphene.String()
    descripcion = graphene.String()
    serie = graphene.String()
    color =  graphene.String()
    transmision =  graphene.String()
    version =  graphene.String()
    precio = graphene.Float()
    numerocilindros = graphene.Int()
    numeropuertas =  graphene.Int()
    combustible =  graphene.String()


    #2
    class Arguments:
        modelo = graphene.String()
        descripcion = graphene.String()
        serie = graphene.String()
        color =  graphene.String()
        transmision =  graphene.String()
        version =  graphene.String()
        precio = graphene.Float()
        numerocilindros = graphene.Int()
        numeropuertas =  graphene.Int()
        combustible =  graphene.String()


    #3
    def mutate(self, info, modelo, descripcion, serie, color, transmision, version,
               precio, numerocilindros, numeropuertas, combustible):
        auto = Auto( 
                     modelo=modelo, 
                     descripcion=descripcion, 
                     serie=serie, 
                     color=color,
                     transmision=transmision, 
                     version=version, 
                     precio=precio, 
                     numerocilindros=numerocilindros, 
                     numeropuertas=numeropuertas,
                     combustible=combustible
                     )
        auto.save() # insert into Auto(...) values (....)

        return CreateAuto(
            id= auto.id,
            modelo= auto.modelo, 
            descripcion= auto.descripcion, 
            serie= auto.serie, 
            color= auto.color,
            transmision= auto.transmision, 
            version= auto.version, 
            precio= auto.precio, 
            numerocilindros= auto.numerocilindros, 
            numeropuertas= auto.numeropuertas,
            combustible= auto.combustible
        )


#4
class Mutation(graphene.ObjectType):
    create_auto = CreateAuto.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


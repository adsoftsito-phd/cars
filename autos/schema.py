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
    numero_cilindros = graphene.Int()
    numero_puertas =  graphene.Int()
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
                     numero_clindros=numerocilindros, 
                     numero_puertas=numeropuertas,
                     combustible=combustible
                     )
        auto.save() # insert into Auto(...) values (....)

        return CreateLink(
            id= auto.id,
            modelo= auto.modelo, 
            description= auto.description, 
            serie= auto.serie, 
            color= auto.color,
            transmision= auto.transmision, 
            version= auto.version, 
            precio= auto.precio, 
            numero_clindros= auto.numero_cilindros, 
            numero_puertas= auto.numero_puertas,
            combustible= auto.combustible
        )


#4
class Mutation(graphene.ObjectType):
    create_auto = CreateAuto.Field()

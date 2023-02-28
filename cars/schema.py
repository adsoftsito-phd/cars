import graphene

import autos.schema


class Query(autos.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)

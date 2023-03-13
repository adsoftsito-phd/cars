import graphene

import autos.schema


class Query(autos.schema.Query, graphene.ObjectType):
    pass

class Mutation(autos.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

import graphene
import core.schema


class Query(core.schema.Query, graphene.ObjectType):
    pass


""" Specify the query schema and type for the Graphene library. """
schema = graphene.Schema(query=Query)

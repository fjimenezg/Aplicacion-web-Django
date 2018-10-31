import graphene
#import adminapp.schema
from app_services import schema, schema2


class Query(schema.Query, schema2.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
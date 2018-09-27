import graphene
#import adminapp.schema
import adminapp.schema2


class Query(adminapp.schema2.Query,  graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
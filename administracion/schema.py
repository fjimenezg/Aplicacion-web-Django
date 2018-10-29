import graphene
#import adminapp.schema
import app_services.schema2


class Query(app_services.schema2.Query,  graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
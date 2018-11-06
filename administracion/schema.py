import graphene
import graphql_jwt
from app_services import schema, schema2

<<<<<<< HEAD

class Query(schema.Query, 
            schema2.Query, 
            graphene.ObjectType):
=======
class Query(schema.Query, schema2.Query, graphene.ObjectType):
>>>>>>> 1a5d20337b768b0525386dca10563145d407db7a
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutations(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
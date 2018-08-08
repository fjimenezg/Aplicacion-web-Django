import graphene
from graphene_django.types import DjangoObjectType
from .models import Service
from .manager_connection import ManagerConnection
from collections import OrderedDict

def create_resolve(field):
    method_str = """def resolve_"""+field+"""(self, info, **kwargs):
    return self['"""+field+"""']
    """
    return method_str

class ResolveField:
    def __init__(self, service_name):
        self.service_name = service_name
        self.service = None
        self.connection = None

    def runConnection(self):
        self.service = Service.objects.filter(service_name=self.service_name)
        if len(self.service) > 0:
            conn_data = self.service[0].connection
            manager_db = conn_data.manager_db
            user = conn_data.user
            passwd = conn_data.passwd
            port = conn_data.port
            hots = conn_data.host
            dbname = conn_data.dbname
            self.connection = ManagerConnection(
                manager_db, user, passwd, port, hots, dbname
            )

    def get_field(self, field, value):
        print("//////////////////////////////")
        self.runConnection()
        if self.connection is not None:       
            data = self.connection.managerSQL(self.service[0].query_sql)
            for fact in data:
                if str(fact[field]) == value:
                    return fact
        return None

    def get_list(self, filter={}):
        print("=================================")
        self.runConnection()
        if self.connection is not None:
            data = self.connection.managerSQL(self.service[0].query_sql)
            if len(filter) > 0:
                for key, value in filter.items():
                    filtered_data = []
                    for fact in data:
                        if str(fact[key]) == str(value):
                            filtered_data.append(fact)
                    data = filtered_data
            return data
        return None

    def getColumns(self):
        print("------------------------------------------------")
        self.runConnection()
        if self.connection is not None:
            data = self.connection.getColumns(self.service[0].query_sql)
            return data
        return None

class OfferType(graphene.ObjectType):

    training = graphene.String()
    tittle = graphene.String()
    length = graphene.String()
    amount = graphene.String()

    def resolve_training(self, info, **kwargs):
        return self['formacion']
    
    def resolve_tittle(self, info, **kwargs):
        return self['titulo']
    
    def resolve_length(self, info, **kwargs):
        return self['duracion']
    
    def resolve_amount(self, info, **kwargs):
        return self['valor']
    
class StudentType(graphene.ObjectType):

    code = graphene.String()
    name = graphene.String()
    program = graphene.String()
    semester = graphene.String()
    
    def resolve_code(self, info, **kwargs):
        return self["codigo_e"]

    def resolve_name(self, info, **kwargs):
        return self["nombre"]

    def resolve_program(self, info, **kwargs):
        return self["programa"]

    def resolve_semester(self, info, **kwargs):
        return self["semestre"]

#================================================================
columns = ResolveField('servicio1').getColumns()
fields = {}
for name in columns:
    fields[name] = graphene.String()
    fields.update({'resolve_'+name:lambda self: self[name]})
type('GenericType',(graphene.ObjectType,),fields)
#=============================================================== 

class Query(graphene.ObjectType):
    fields_service = ResolveField('servicio1').getColumns()
    clsattr_service = {}
    for field in fields_service:
        clsattr_service.update({field:graphene.String()})
        attr = {}
        exec(create_resolve(field), globals(), attr)
        clsattr_service.update(attr)

    student = graphene.Field(StudentType, code=graphene.String())
    offer = graphene.Field(OfferType, code=graphene.String())

    c = {'semestre':graphene.String(), 'programa':graphene.String()}

    all_students = graphene.List(type('StudentType2',(graphene.ObjectType,),clsattr_service), c)
    all_offers = graphene.List(OfferType)

    def resolve_student(self, info, **kwargs):
        code = kwargs.get("code")
        if code is not None:
            return ResolveField("servicio1").get_field("codigo_e", code)
    
    def resolve_offer(self, info, **kwargs):
        code = kwargs.get("code")
        if code is not None:
            return ResolveField("servicio2").get_field("codigo", code)

    def resolve_all_students(self, info, **kwargs):
        return ResolveField("servicio1").get_list(kwargs)

    def resolve_all_offers(self, info, **kwargs):
        return ResolveField("servicio2").get_list()



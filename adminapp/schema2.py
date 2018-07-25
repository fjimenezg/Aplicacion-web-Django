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

def create_resolve_query(service_name):
    method_str = """def resolve_"""+service_name+"""(self, info, **kwargs):
    return ResolveField('"""+service_name+"""').get_list()
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

    def get_list(self):
        print("=================================")
        self.runConnection()
        if self.connection is not None:
            data = self.connection.managerSQL(self.service[0].query_sql)
            listData = [data for data in data]
            return listData
        return None

    def getColumns(self):
        print("------------------------------------------------")
        self.runConnection()
        if self.connection is not None:
            data = self.connection.getColumns(self.service[0].query_sql)
            return data
        return None


clsattr_query= {}
clsattr_service = {}

services = Service.objects.all()

for service in services:
    fields_service = ResolveField(service.service_name).getColumns()
    clsattr_service.clear()

    for field in fields_service:
        clsattr_service.update({field:graphene.String()})
        attr = {}
        exec(create_resolve(field), globals(), attr)
        clsattr_service.update(attr)


    clsattr_query.update({service.service_name:graphene.List(
        type(service.service_name, (graphene.ObjectType,), clsattr_service)
    )})

    attr = {}
    exec(create_resolve_query(service.service_name), globals(), attr)
    clsattr_query.update(attr)

Query = type('Query', (graphene.ObjectType,), clsattr_query)
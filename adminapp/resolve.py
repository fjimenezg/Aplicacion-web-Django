from .models import Service
from .manager_connection import ManagerConnection

def resolve_field(field):
    method_str = """def resolve_"""+field+"""(self, info, **kwargs):
    return self['"""+field+"""']
    """
    return method_str

def resolve_service(service):
    method_str = """def resolve_"""+service+"""(self, info, **kwargs):
    return ResolveService('"""+service+"""').get_list(kwargs)
    """
    return method_str

class ResolveService:
    def __init__(self, service):
        if type(service) == str:
            try:
                self.service = Service.objects.get(service_name=service)
            except:
                self.service = None
        else:
            self.service = service
        self.connection = None
        self.runConnection()

    def is_active(self):
        return self.connection.check_connection()

    def runConnection(self):
            conn_data = self.service.connection
            manager_db = conn_data.manager_db
            user = conn_data.user
            passwd = conn_data.passwd
            port = conn_data.port
            hots = conn_data.host
            dbname = conn_data.dbname
            self.connection = ManagerConnection(
                manager_db, user, passwd, port, hots, dbname
            )

    def get_field(self, key, value):
        if self.is_active():       
            data = self.connection.managerSQL(self.service.query_sql)
            for fact in data:
                if str(fact[key]) == value:
                    return fact
        return None

    def get_list(self, filter={}):
        if self.is_active():
            data = self.connection.managerSQL(self.service.query_sql)
            if len(filter) > 0:
                for key, value in filter.items():
                    filtered_data = []
                    for fact in data:
                        if str(fact[key]) == str(value):
                            filtered_data.append(fact)
                    data = filtered_data
            return data
        return None

    def get_columns(self):
        if self.is_active():
            data = self.connection.getColumns(self.service.query_sql)
            return data
        return None

from .models import Service
from .manager_connection import ManagerConnection

def resolve_field(field):
    method_str = """def resolve_"""+field+"""(self, info, **kwargs):
    return self['"""+field+"""']
    """
    return method_str

def resolve_service(service, filter=None):
    if filter is not None:
        method_str = """def resolve_"""+service+"""(self, info, **kwargs):
        kwargs['"""+filter[1]+"""'] = self['"""+filter[0]+"""']
        return Service.objects.get(service_name='"""+service+"""').get_list_search(kwargs)
        """
    else:
        method_str = """def resolve_"""+service+"""(self, info, **kwargs):
        return Service.objects.get(service_name='"""+service+"""').get_list_search(kwargs)
        """
    return method_str


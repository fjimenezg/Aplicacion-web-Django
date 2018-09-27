from .models import Service
from .manager_connection import ManagerConnection

def resolve_field(field):
    method_str = """def resolve_"""+field+"""(self, info, **kwargs):
    return self['"""+field+"""']
    """
    return method_str

def resolve_service_query(service):
    method_str = """def resolve_"""+service+"""(self, info, **kwargs):
    service = Service.objects.get(service_name='"""+service+"""')
    return service.get_list_search(kwargs)
    """
    return method_str

def batch_load_fn(service):
    batch_load_fn = """def batch_load_fn(self, keys):
    service = Service.objects.get(service_name='"""+service+"""')
    return Promise.resolve([service.get_list_search(ast.literal_eval(key))for key in keys])
    """
    return batch_load_fn

def resolve_service_loader(service, filter={}):
    method_str = """def resolve_"""+service+"""(self, info, **kwargs):
    kwargs['"""+filter[1]+"""'] = self['"""+filter[0]+"""']
    return dict_dataloader['"""+service+"""'].load(str(kwargs))
    """
    return method_str

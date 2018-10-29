import graphene
from .models import Service
from .resolve import *
from promise import Promise
from promise.dataloader import DataLoader

services = Service.objects.all()
dict_types = {}
dict_clsattr_query = {}
dict_dataloader = {}


def build_loader(service):
    attr = {}
    exec(batch_load_fn(service.service_name), globals(), attr)
    loader = type("DataLoader", (DataLoader,), attr)
    dict_dataloader.update({service.service_name: loader()})


# Esta funcion crea un diccionario con los campos y funciones resolvedoras de un servicio
def build_dict_fields(service):
    clsattr_service = {}

    clsattr_service.update({"name": graphene.String()})
    clsattr_service.update({"key": graphene.String()})
    clsattr_service.update({"icon": graphene.String()})
    clsattr_service.update(
        {
            "data": graphene.List(
                build_type(service),
                dict.fromkeys(service.get_fields_service(), graphene.String()),
            )
        }
    )

    clsattr_service.update(
        {"resolve_name": lambda self, info, **kwargs: self.service_name}
    )
    clsattr_service.update(
        {"resolve_key": lambda self, info, **kwargs: self.unique_key}
    )
    clsattr_service.update(
        {"resolve_icon": lambda self, info, **kwargs: self.icon}
    )
    clsattr_service.update(
        {"resolve_data": lambda self, info, **kwargs: self.get_list_search(kwargs)}
    )

    return clsattr_service


def build_service(service):
    if service not in dict_types:
        dict_types.update(
            {
                service: type(
                    service.type_name,
                    (graphene.ObjectType,),
                    build_dict_fields(service),
                )
            }
        )
    return dict_types[service]


def build_type(service):
    clsattr_service = {}
    fields_service = service.get_fields_service()

    if fields_service is not None:
        for field in fields_service:
            clsattr_service.update({field: graphene.String()})
            attr = {}
            clsattr_service.update(
                {"resolve_" + field: lambda self, info, **kwargs: self[info.field_name]}
            )

        links = service.get_links()
        if links is not None:
            for key, value in links.items():
                linked_service = Service.objects.get(service_name=key)
                clsattr_service.update(
                    {
                        key: graphene.List(
                            build_service(linked_service),
                            dict.fromkeys(
                                linked_service.get_fields_service(), graphene.String()
                            ),
                        )
                    }
                )

                attr = {}
                exec(resolve_service_loader(key, value), globals(), attr)
                clsattr_service.update(attr)

                build_loader(linked_service)

    return type(service.type_name + "Data", (graphene.ObjectType,), clsattr_service)


def build_clsattr_query():
    for service in services:
        if service.is_active():
            try:
                dict_clsattr_query.update(
                    {service.type_name: graphene.Field(build_service(service))}
                )

                dict_clsattr_query.update(
                    {
                        "resolve_"
                        + service.type_name: lambda self, info, **kwargs: Service.objects.get(
                            type_name=info.field_name
                        )
                    }
                )
            except:
                print("Algo salio mal")


build_clsattr_query()
Query = type("Query", (graphene.ObjectType,), dict_clsattr_query)
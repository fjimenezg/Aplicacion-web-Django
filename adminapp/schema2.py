import graphene
from .models import Service
from .resolve import resolve_field, resolve_service_query, batch_load_fn, resolve_service_loader
from promise import Promise
from promise.dataloader import DataLoader
import ast
import asyncio

services = Service.objects.all()
dict_types = {}
dict_clsattr_query = {}
dict_dataloader = {}

def build_loader(service):
    attr = {}
    exec(batch_load_fn(service.service_name), globals(), attr)
    loader = type("DataLoader", (DataLoader,), attr)
    dict_dataloader.update(
        {service.service_name: loader()}
    )


# Esta funcion crea un diccionario con los campos y funciones resolvedoras de un servicio
def build_dict_fields(service):
    clsattr_service = {}
    fields_service = service.get_fields_service()

    if fields_service is not None:
        for field in fields_service:
            clsattr_service.update({field: graphene.String()})
            attr = {}
            exec(resolve_field(field), globals(), attr)
            clsattr_service.update(attr)

        links = service.get_links()
        if links is not None:
            for key, value in links.items():
                linked_service = Service.objects.get(service_name=key)
                clsattr_service.update(
                    {
                        key: graphene.List(
                            build_type(linked_service),
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

    return clsattr_service


def build_type(service):
    if service not in dict_types:
        dict_types.update(
            {
                service: type(
                    service.class_name,
                    (graphene.ObjectType,),
                    build_dict_fields(service),
                )
            }
        )
    return dict_types[service]


def build_clsattr_query():
    for service in services:
        if service.is_active():
            dict_clsattr_query.update(
                {
                    service.service_name: graphene.List(
                        build_type(service),
                        dict.fromkeys(service.get_fields_service(), graphene.String()),
                    )
                }
            )

            attr = {}
            exec(resolve_service_query(service.service_name), globals(), attr)
            dict_clsattr_query.update(attr)


build_clsattr_query()
Query = type("Query", (graphene.ObjectType,), dict_clsattr_query)

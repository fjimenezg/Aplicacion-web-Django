import graphene
from graphene_django.types import DjangoObjectType
from .models import Service
from .resolve import resolve_field, resolve_service, ResolveService

services = Service.objects.all()
clsattr_query = {}

for service in services:
    resolve = ResolveService(service)

    if resolve.is_active():
        fields_service = resolve.get_columns()
        clsattr_service = {}

        for field in fields_service:
            clsattr_service.update({field: graphene.String()})
            attr = {}
            exec(resolve_field(field), globals(), attr)
            clsattr_service.update(attr)

        clsattr_query.update(
            {
                service.service_name: graphene.List(
                    type(service.service_name, (graphene.ObjectType,), clsattr_service),
                    dict.fromkeys(service.get_items_list(), graphene.String()),
                )
            }
        )

        attr = {}
        exec(resolve_service(service.service_name), globals(), attr)
        clsattr_query.update(attr)

Query = type("Query", (graphene.ObjectType,), clsattr_query)


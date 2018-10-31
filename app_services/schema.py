import graphene
from graphene_django.types import DjangoObjectType
from .models import Service, Location, MissingItem, Office, SQLQuery

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service

class LocationType(DjangoObjectType):
    class Meta:
        model = Location

class MissingItemType(DjangoObjectType):
    class Meta:
        model = MissingItem

class OfficeType(DjangoObjectType):
    class Meta:
        model = Office


class Query(graphene.AbstractType):
    all_services = graphene.List(ServiceType,kind=graphene.String())
    all_locations = graphene.List(LocationType,id=graphene.Int())
    all_items = graphene.List(MissingItemType,id=graphene.Int())
    all_offices = graphene.List(OfficeType,id=graphene.Int())
    service = graphene.Field(ServiceType,id=graphene.Int())
    location = graphene.Field(LocationType,id=graphene.Int())
    item = graphene.Field(MissingItemType,id=graphene.Int())
    office = graphene.Field(OfficeType,id=graphene.Int())

    def resolve_all_services(self, info, **kwargs):
        kind = kwargs.get('kind')
        if kind is not None:
            return Service.objects.all().filter(kind=kind)
        
        return Service.objects.all()

    def resolve_all_locations(self, info, **kwargs):
        id = kwargs.get('id')
        source = None

        if id is not None:
            source = Service.objects.get(pk=id)

        if source is not None:
            return Location.objects.all().filter(Service=source)

        return Location.objects.all()

    def resolve_all_items(self, info, **kwargs):
        id = kwargs.get('id')
        source = None

        if id is not None:
            source = Service.objects.get(pk=id)

        if source is not None:
            return MissingItem.objects.all().filter(Service=source)

        return MissingItem.objects.all()

    def resolve_all_offices(self, info, **kwargs):
        id = kwargs.get('id')
        source = None

        if id is not None:
            source = Service.objects.get(pk=id)

        if source is not None:
            return Office.objects.all().filter(Service=source)

        return Office.objects.all()

    def resolve_service(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Service.objects.get(pk=id)

        return None

    def resolve_location(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Location.objects.get(pk=id)

        return None

    def resolve_item(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return MissingItem.objects.get(pk=id)

        return None

    def resolve_office(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Office.objects.get(pk=id)

        return None
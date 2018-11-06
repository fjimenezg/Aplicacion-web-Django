import graphene
from graphene_django.types import DjangoObjectType
from .models import *

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

class PermitsType(DjangoObjectType):
    class Meta:
        model = Permits

class IconType(DjangoObjectType):
    class Meta:
        model = Icon

class KindType(DjangoObjectType):
    class Meta:
        model = Kind

class Directory(graphene.ObjectType):
    title = graphene.String()
    icon = graphene.String()
    permits = graphene.Field(PermitsType)
    state = graphene.String()
    description = graphene.String()
    phone = graphene.List(OfficeType)

    def resolve_title(self, info, **kwargs):
        return self.title

    def resolve_icon(self, info, **kwargs):
        return self.title
    
    def resolve_phone(self, info, **kwargs):
        return Office.objects.all().filter(service=self)

class Directories(graphene.ObjectType):
    directory = graphene.Field(Directory)

    def resolve_directory(self, info, **kwargs):
        return self

class Query(graphene.AbstractType):
    directories = graphene.List(Directories, title=graphene.String())
    get_all_services = graphene.List(ServiceType,kind=graphene.String())

    get_map = graphene.List(LocationType,id=graphene.Int())
    get_catalog = graphene.List(MissingItemType,id=graphene.Int())
    get_directory = graphene.List(OfficeType,id=graphene.Int())

    get_icon = graphene.List(IconType,id=graphene.Int())
    get_kind = graphene.List(IconType,id=graphene.Int())
    get_permits = graphene.List(PermitsType,id=graphene.Int())

    get_service = graphene.Field(ServiceType,id=graphene.Int())
    get_location = graphene.Field(LocationType,id=graphene.Int())
    get_item = graphene.Field(MissingItemType,id=graphene.Int())
    get_office = graphene.Field(OfficeType,id=graphene.Int())

    def resolve_get_all_services(self, info, **kwargs):
        kind = kwargs.get('kind')
        if kind is not None:
            return Service.objects.all().filter(kind=kind)
        
        return Service.objects.all()

    def resolve_get_map(self, info, **kwargs):
        id = kwargs.get('id')
        source = None

        if id is not None:
            source = Service.objects.get(pk=id)

        if source is not None:
            return Location.objects.all().filter(service=source)

        return Location.objects.all()

    def resolve_get_catalog(self, info, **kwargs):
        id = kwargs.get('id')
        source = None

        if id is not None:
            source = Service.objects.get(pk=id)

        if source is not None:
            return MissingItem.objects.all().filter(service=source)

        return MissingItem.objects.all()

    def resolve_get_directory(self, info, **kwargs):
        id = kwargs.get('id')
        source = None

        if id is not None:
            source = Service.objects.get(pk=id)

        if source is not None:
            return Office.objects.all().filter(service=source)

        return Office.objects.all()

    def resolve_get_icon(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Service.objects.get(pk=id).icon    

        return Icons.objects.all()

    def resolve_get_kind(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Service.objects.get(pk=id).kind  

        return Kind.objects.all()

    def resolve_get_permits(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Service.objects.get(pk=id).permits   

        return Permits.objects.all()

    def resolve_get_service(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Service.objects.get(pk=id)

        return None

    def resolve_get_location(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Location.objects.get(pk=id)

        return None

    def resolve_get_item(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return MissingItem.objects.get(pk=id)

        return None

    def resolve_get_office(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Office.objects.get(pk=id)

        return None

    def resolve_directories(self, info, **kwargs):
        title = kwargs.get('title')
        if title is not None:
            return Service.objects.all().filter(kind=2, title=title)
        return Service.objects.all().filter(kind=2)
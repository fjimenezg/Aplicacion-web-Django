import graphene
from graphene_django.types import DjangoObjectType
from .models import Service
from global_.manager_connection import ManagerConnection
from collections import OrderedDict

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

class Grades(graphene.ObjectType):
    grade = graphene.String()
    subject = graphene.String()
    codigoEstudiante = graphene.String()

    def resolve_grade(self, info, **kwargs):
        return self['nota']

    def resolve_subject(self, info, **kwargs):
        return self['codigo_materia']
    
    def resolve_codigoEstudiante(self, info, **kwargs):
        return self['codigoEstudiante']

    
class StudentType(graphene.ObjectType):

    code = graphene.String()
    name = graphene.String()
    program = graphene.String()
    semester = graphene.String()
    grades = graphene.List(Grades, code=graphene.String())

    
    def resolve_code(self, info, **kwargs):
        return self["codigo"]

    def resolve_name(self, info, **kwargs):
        print(self)
        return self["nombres"]

    def resolve_semester(self, info, **kwargs):
        return self["semestre"]

    def resolve_grades(self, info, **kwargs):
        kwargs['codigoEstudiante'] = self['codigo']
        return ResolveField("servicio3").get_list(kwargs)


class Query(graphene.ObjectType):
    student = graphene.Field(StudentType, code=graphene.String())
    offer = graphene.Field(OfferType, code=graphene.String())

    c = {'semestre':graphene.String(), 'programa':graphene.String(), 'codigo':graphene.String()}

    all_students = graphene.List(StudentType, c)
    all_offers = graphene.List(OfferType)
    Grades = graphene.List(Grades)

    def resolve_student(self, info, **kwargs):
        code = kwargs.get("code")
        if code is not None:
            return ResolveField("servicio4").get_field("codigo", code)
    
    def resolve_offer(self, info, **kwargs):
        code = kwargs.get("code")
        if code is not None:
            return ResolveField("servicio2").get_field("codigo", code)

    def resolve_all_students(self, info, **kwargs):
        print(ResolveField("servicio4").get_list(kwargs))
        return ResolveField("servicio4").get_list(kwargs)

    def resolve_all_offers(self, info, **kwargs):
        return ResolveField("servicio2").get_list()

    def resolve_Grades(self, info, **kwargs):
        return ResolveField("servicio2").get_list()

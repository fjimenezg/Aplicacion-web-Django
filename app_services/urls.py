from django.urls import path
from .views import *
from graphene_django.views import GraphQLView


urlpatterns = [
    path(
        'service',
        base_service,
        name='base-service'
    ),

    path(
        'service/create',
        ServiceCreateView.as_view(),
        name='create-service'
    ),

    path(
        'service/list',
        ServiceListView.as_view(),
        name='list-service'
    ), 
    path(
        'service/fields',
        get_fields_service,
        name='fields-service'
    )
]

from django.urls import path, include
from .views import *

urlpatterns = [
    # Servicio
    path('services/', base_service, name='base-service'),
    path('services/list', ServiceListView.as_view(), name='service-list'),
    path('services/create', ServiceCreateView.as_view(), name='service-create'),
    path('services/<int:pk>/edit', ServiceUpdateView.as_view(), name='service-edit'),   
    path('services/<int:pk>/delete', ServiceDeleteView.as_view(), name='service-delete'),

    # Catalogo de objetos perdidos
    path('services/items/list', MissingItemListView.as_view(), name='item-list'),
    path('services/items/<int:service_id>/configure', item_configure, name='item-configure'),
    path('services/items/<int:service_id>/create', item_create, name='item-create'),
    path('services/items/<int:service_id>/<int:pk>/edit', MissingItemUpdateView.as_view(), name='item-edit'),   
    path('services/items/<int:service_id>/<int:pk>/delete', MissingItemDeleteView.as_view(), name='item-delete'),

    # Directorio de dependencias
    path('services/offices/list', OfficeListView.as_view(), name='office-list'),
    path('services/offices/<int:service_id>/configure', office_configure, name='office-configure'),
    path('services/offices/<int:service_id>/create', office_create, name='office-create'),
    path('services/offices/<int:service_id>/<int:pk>/edit', OfficeUpdateView.as_view(), name='office-edit'),   
    path('services/offices/<int:service_id>/<int:pk>/delete', OfficeDeleteView.as_view(), name='office-delete'),

    # Mapa de Bloques
    path('services/locations/list', LocationListView.as_view(), name='location-list'),
    path('services/locations/<int:service_id>/configure', location_configure, name='location-configure'),
    path('services/locations/<int:service_id>/create', location_create, name='location-create'),
    path('services/locations/<int:service_id>/<int:pk>/edit', LocationUpdateView.as_view(), name='location-edit'),   
    path('services/locations/<int:service_id>/<int:pk>/delete', LocationDeleteView.as_view(), name='location-delete'),

    # Consulta SQL
    path('services/query/<int:service_id>/configure', QueryCreateView.as_view(), name='query-configure'),
    path(
        'services/query/fields',
        get_fields_service,
        name='fields-service'
    )

]
from django.urls import path
from .. views import views_01Connection

urlpatterns = [
    path('connection/', views_01Connection.base_connection, name='base-connection'),
    path('connection/listdb', views_01Connection.list_db, name='list-db'),
    path('connection/<int:id_connection>/check', views_01Connection.check_connection, name='check-connection'),
    path('connection/create', views_01Connection.ConnectionCreateView.as_view(), name='create-connection'),
    path('connection/<int:pk>/edit', views_01Connection.ConnectionUpdateView.as_view(), name='edit-connection'),   
    path('connection/list', views_01Connection.ConnectionListView.as_view(), name='list-connections'),
    path('connection/<int:pk>/delete', views_01Connection.ConnectionDeleteView.as_view(), name='delete-connection'),
]
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from adminapp.models import Connection
from .. forms import ConnectionForm
from .. manager_connection import ManagerConnection
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.


def base_connection(request):
    return render(request, "01Connection/base.html")

class ConnectionCreateView(CreateView):
    model = Connection
    form_class = ConnectionForm
    template_name = "01Connection/connection_form.html"


class ConnectionUpdateView(UpdateView):
    model = Connection
    form_class = ConnectionForm
    template_name = "01Connection/connection_form.html"


class ConnectionListView(ListView):
    model = Connection
    template_name = "01Connection/connection_list.html"


class ConnectionDeleteView(DeleteView):
    model = Connection
    template_name = "01Connection/delete_connection.html"
    success_url = reverse_lazy('list-connections')


# Crear la vista para listar las base de datos con los parametros ingresados en el ssitema.

def list_db(request):
    manager_db = request.POST['manager_db']
    user = request.POST['user']
    passwd = request.POST['passwd']
    port = request.POST['port']
    host = request.POST['host']

    conn = ManagerConnection(manager_db,user,passwd,port,host)
    context = {}
    dblist = conn.list_db()      
    if dblist is not None:                
        context =  {'object_list':dblist} 
    return JsonResponse(context)

def check_connection(request, id_connection):
    connection = Connection.objects.get(id=id_connection)
    conn = ManagerConnection(connection.manager_db,connection.user,connection.passwd,connection.port,connection.host,connection.dbname)        
    context =  {'object':conn.check_connection()}
    return JsonResponse(context) 
    
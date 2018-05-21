from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from adminapp.models import Connection
from .. manager_connection import Manager
from django.urls import reverse_lazy

# Create your views here.

def base_connection(request):
    return render(request, "01Connection/base.html")

class ConnectionCreateView(CreateView):
    model = Connection
    fields = '__all__'
    template_name = "01Connection/connection_form.html"


class ConnectionUpdateView(UpdateView):
    model = Connection
    fields = '__all__'
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

    conn = Manager(manager_db,user,passwd,port,host)
    context = {}

    if manager_db == 'mysql':
        dblist = conn.list_db() 
        print(dblist)
        if dblist is not None:                
            context =  {'object_list':dblist}
        return render(request, '01Connection/check_connection.html', context)
    if manager_db == 'postgres':
        pass
    if manager_db == 'oracle':
        pass
    
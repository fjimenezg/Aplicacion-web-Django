from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Service
from app_connection.models import Connection
from .forms import ServiceForm
from django.http import JsonResponse
from global_.manager_connection import ManagerConnection

# Create your views here.


def base_service(request):
    return render(request, "02Service/base.html")


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "02Service/service_form.html"


class ServiceListView(ListView):
    model = Service
    template_name = "02Service/service_list.html"


def get_fields_service(request):
    query_sql = request.POST["query_sql"]
    id_connection = request.POST["connection"]

    connection = Connection.objects.get(id=id_connection)
    data_conecction = connection.get_data_connection()
    conn = ManagerConnection(**data_conecction)
    fields_service = conn.getColumns(query_sql)

    context = {"object_list": fields_service}
    return JsonResponse(context)

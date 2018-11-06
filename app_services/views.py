from django.shortcuts import render,redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.http import JsonResponse

def base_service(request):
    return render(request, "Services/base.html")

# Servicio
class ServiceListView(ListView):
    model = Service
    template_name = "Services/service_list.html"

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service-list')


# Catalogo de objetos perdidos
def item_configure(request,service_id):
    service = Service.objects.get(pk=service_id)
    items = MissingItem.objects.all().filter(service=service)
    return render(request, 'Services/item_configure.html', {'object_list':items,'service':service})

def item_create(request,service_id):
    success_url = reverse_lazy('service-list')
    if request.method == 'POST':
        form = MissingItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Service = Service.objects.get(pk=service_id)
            post.save()
            return render(request, 'Services/item_form.html')

    else: 
        form = MissingItemForm()
        return render(request, 'Services/item_form.html', {'form':form, 'service_id':service_id})

class MissingItemListView(ListView):
    model = MissingItem
    template_name = "Services/item_detail.html"

class MissingItemCreateView(CreateView):
    model = MissingItem
    fields = '__all__'
    #form_class = MissingItemForm
    #template_name = "Services/item_form.html"

class MissingItemUpdateView(UpdateView):
    model = MissingItem
    fields = '__all__'
    #form_class = MissingItemForm
    #template_name = "Services/item_form.html"

class MissingItemDeleteView(DeleteView):
    model = MissingItem
    success_url = reverse_lazy('service-list')


# Directorio de dependencias
def office_configure(request,service_id):
    service = Service.objects.get(pk=service_id)
    offices = Office.objects.all().filter(service=service)
    return render(request, 'Services/office_configure.html', {'object_list':offices,'service':service})

def office_create(request,service_id):
    success_url = reverse_lazy('service-list')
    if request.method == 'POST':
        form = OfficeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Service = Service.objects.get(pk=service_id)
            post.save()
            return render(request, 'Services/office_form.html')

    else: 
        form = OfficeForm()
        return render(request, 'Services/office_form.html', {'form':form, 'service_id':service_id})

class OfficeListView(ListView):
    model = Office
    template_name = "Services/office_list.html"

class OfficeCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class OfficeUpdateView(UpdateView):
    model = Office
    success_url = reverse_lazy('service-list')
    form_class = OfficeForm
    template_name = "Services/office_form.html"

class OfficeDeleteView(DeleteView):
    model = Office
    success_url = reverse_lazy('service-list')

# Mapa de bloques
def location_configure(request,service_id):
    service = Service.objects.get(pk=service_id)
    locations = Location.objects.all().filter(service=service)
    return render(request, 'Services/location_configure.html', {'object_list':locations,'service':service})

def location_create(request,service_id):
    success_url = reverse_lazy('service-list')
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Service = Service.objects.get(pk=service_id)
            post.save()
            return render(request, 'Services/location_form.html')

    else: 
        form = LocationForm()
        return render(request, 'Services/location_form.html', {'form':form, 'service_id':service_id})

class LocationListView(ListView):
    model = Location
    template_name = "Services/location_list.html"

class LocationCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class LocationUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "Services/service_form.html"

class LocationDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service-list')


# Consulta SQL

class QueryCreateView(CreateView):
    model = SQLQuery
    form_class = QueryForm
    template_name = "Services/query_configure.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.service = Service.objects.get(id=self.kwargs["service_id"])
        self.object.save()
        return super(QueryCreateView, self).form_valid(form)


def get_fields_service(request):
    query_sql = request.POST["query_sql"]
    id_connection = request.POST["connection"]

    connection = Connection.objects.get(id=id_connection)
    data_conecction = connection.get_data_connection()
    conn = ManagerConnection(**data_conecction)
    fields_service = conn.getColumns(query_sql)

    context = {"object_list": fields_service}
    return JsonResponse(context)


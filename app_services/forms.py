from django import forms
from .models import *

# Formulario para gestionar conexión.
class QueryForm(forms.ModelForm):
    class Meta:

        model = SQLQuery

        fields = [
            "connection",
            "type_name",
            "query_sql",
        ]

        labels = {
            "connection": "Conexión a la base de datos",
            "type_name": "Nombre de clase",
            "query_sql": "Sentencia de datos sql",
        }

        error_messages = {
            "type_name": {"unique": "El nombre de la clase ya existe"},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})


# Formulario para gestionar conexión.
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "kind", "roles", "state"]
        error_messages = {"name": {"unique": "El nombre del servicio ya existe."}}


# Formulario para gestionar artículos perdidos.
class MissingItemForm(forms.ModelForm):
    class Meta:
        model = MissingItem
        fields = ["name", "Service", "description", "photo"]
        labels = {
            "name": "Nombre",
            "Service": "Servicio asociado",
            "description": "Descripcion",
            "photo": "Foto",
        }
        error_messages = {"name": {"unique": "El nombre del objeto ya existe."}}


# Formulario para gestionar directorio de names.
class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office

        fields = ["name", "extension", "phone"]

        labels = {"name": "Nombre", "extension": "Extension", "phone": "Telefono"}

        """widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'extension':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }"""


# Formulario para gestionar locaclizaciones.
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location

        fields = ["name", "longitude", "latitude"]

        labels = {"name": "Nombre", "longitude": "Longitud", "latitude": "Latitud"}

        """
        widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'longitude':forms.TextInput(attrs={'class':'form-control'}),
            'latitude':forms.TextInput(attrs={'class':'form-control'}),
        }"""


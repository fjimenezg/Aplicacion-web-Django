# -*- coding: utf-8 -*-
from django import forms
from .models import Service

#Formulario para gestionar conexión.
class ServiceForm(forms.ModelForm):
    
    class Meta:

        model = Service 

        fields = [
            'connection',
            'service_name',
            'type_name',
            'query_sql',
            'icon',
            'unique_key'
        ]

        labels = {
            'connection':'Conexión a la base de datos',
            'service_name':'Nombre del servicio',
            'type_name':'Nombre de clase',
            'query_sql':'Sentencia de datos sql',
        }

        error_messages = {
            'service_name': {
                'unique':"El nombre del servicio ya existe.",
            },
            'type_name':{
                'unique':'El nombre de la clase ya existe'
            }
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        


        
        
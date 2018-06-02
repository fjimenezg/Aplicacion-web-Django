# -*- coding: utf-8 -*-
from django import forms
from adminapp.models import Connection

#Formulario para gestionar conexión.
class ConnectionForm(forms.ModelForm):

    class Meta:

        model = Connection

        fields = [
            'connection_name',
            'manager_db',
            'port',
            'host',
            'user',
            'passwd',
            'dbname',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Recorremos todos los campos del modelo para añadirle class="form-control
            if field == "passwd":
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            else:
                self.fields[field].widget.attrs.update({'class': 'form-control','required':'required'})
        
        
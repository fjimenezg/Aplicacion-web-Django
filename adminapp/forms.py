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
            self.fields[field].widget.attrs.update({'class': 'form-control','required':'required'})
        
        self.fields['passwd'].widget.attrs.update({'class': 'form-control','required':'false'})
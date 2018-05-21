# -*- coding: utf-8 -*-
from django import forms
from adminapp.models import Conexion, Sql, Directorio, Localizacion, Articulo

#Formulario para gestionar conexión.
class ConexionForm(forms.ModelForm):

    class Meta:
        model = Conexion

        fields = [
            'nombre',
            'ip',
            'puerto',
            'motor',
            'usuario',
            'contrasena',
            'bd',
        ]

        labels={
            'nombre':'nombre bd',
            'ip': 'ip bd',
            'puerto': 'puerto bd', 
            'motor': 'motor bd',
            'usuario': 'usuario bd',
            'contrasena': 'contrasena bd',
            'bd': 'base de datos',
        }
        widget={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'ip' :forms.TextInput(attrs={'class':'form-control'}),
            'puerto' :forms.TextInput(attrs={'class':'form-control'}),
            'motor' :forms.TextInput(attrs={'class':'form-control'}),
            'usuario' :forms.TextInput(attrs={'class':'form-control'}),
            'contrasena' :forms.TextInput(attrs={'class':'form-control'}),
            'bd' :forms.TextInput(attrs={'class':'form-control'}),
        }
#Formulario para gestionar servicios.
class ServicioForm(forms.ModelForm):

    class Meta:
        model = Sql

        fields = [
            'conexion',
            'rol',
            'nombre',
            'sql',
            'descripcion',
        ]

        labels={
            'conexion':'nombre conexion',
            'rol':'rol',
            'nombre':'nombre',
            'sql':'sql',
            'descripcion': 'descripcion', 
        }
        widget={
            'conexion':forms.ModelChoiceField(queryset=Conexion.objects.all()),
            'rol' :forms.TextInput(attrs={'class':'form-control'}),
            'nombre' :forms.TextInput(attrs={'class':'form-control'}),
            'sql' :forms.Textarea(attrs={'class':'form-control'}),
            'descripcion' :forms.Textarea(attrs={'class':'form-control'}),
        }
#Formulario para gestionar directorio telefónico.        
class DirectorioForm(forms.ModelForm):
    
    class Meta:
        model = Directorio
        
        fields = [
            'dependencia',
            'extension',
            'linea_directa',
        ]
        
        labels={
            'dependencia':'nombre dependencia',
            'extension':'extension',
            'linea_directa':'linea directa',
        }
        
        widget={
            'dependencia':forms.TextInput(attrs={'class':'form-control'}),
            'extension':forms.TextInput(attrs={'class':'form-control'}),
            'linea_directa':forms.TextInput(attrs={'class':'form-control'}),
        }
#Formulario para gestionar locaclizaciones.      
class LocalizacionForm(forms.ModelForm):
    
    class Meta:
        model = Localizacion
        
        fields = [
            'descripcion',
            'longitud',
            'latitud',
        ]
        
        labels={
            'descripcion':'descripcion',
            'longitud':'longitud',
            'latitud':'latitud',
        }
        
        widget={
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'longitud':forms.TextInput(attrs={'class':'form-control'}),
            'latitud':forms.TextInput(attrs={'class':'form-control'}),
        }

#Formulario para gestionar artículos perdidos.
class ArticuloForm(forms.ModelForm):
    
    class Meta:
        model = Articulo
        
        fields = [
            'descripcion',
            'fecha',
            'foto',
        ]
        
        labels={
            'descripcion':'descripcion',
            'fecha':'fecha',
            'foto':'foto',
        }
        
        widget={
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'fecha':forms.DateField( widget=forms.widgets.DateInput(format="%m/%d/%Y")),
            'foto':forms.TextInput(attrs={'class':'form-control'}),
        }
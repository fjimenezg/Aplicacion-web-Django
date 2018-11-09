from django.db import models
from django.contrib.auth.models import User
from app_services.models import Group

class UserGroups(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='get_groups')
    groups = models.ManyToManyField(Group, related_name='get_users')
    

    # * usando related_name personalizado:  
    # ==> Lista_de_grupos = User.get_groups.groups.all()

    # * usando related_name por defecto (hay que borrar <related_name='get_groups'>):  
    # ==> Lista_de_grupos = user.usergroups.groups.all()

    # * tambien podemos obtener, a partir de una instancia de grupo,
    #    todos los usuarios que pertenecen a ese grupo
    # ==> Lista_de_usuarios = group.get_users.all()

    # * ejemplo generico
    # ==> Lista_generica = modelopadre.modelohijo.parametro
    
    

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.user.username


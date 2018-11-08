from django.db import models
from django.contrib.auth.models import User
from app_services.models import Group

class UserGroups(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='get_user')
    groups = models.ManyToManyField(Group, related_name='get_groups')
    

    #User.get_user.get_groups.all
    #user.usergroups.group.all

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.user.username


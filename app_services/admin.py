from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Service)
admin.site.register(SQLQuery)
admin.site.register(Office)
admin.site.register(Location)
admin.site.register(MissingItem)
admin.site.register(Icon)
admin.site.register(Kind)
admin.site.register(Group)
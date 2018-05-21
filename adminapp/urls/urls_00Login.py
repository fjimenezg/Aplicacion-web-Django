from django.urls import path
from .. views import views_00Login

urlpatterns = [
    path('', views_00Login.login, name='login'),
]

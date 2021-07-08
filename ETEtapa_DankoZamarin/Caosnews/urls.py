from django.urls import path
from .views import index, form_ver, form_eliminar, form_crear, form_modificar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('form_ver', form_ver, name="form_ver"),
    path('form_crear', form_crear, name="form_crear"),
    path('form_modificar/<id>', form_modificar, name="form_modificar"),
    path('form_eliminar/<id>', form_eliminar, name="form_eliminar"),

]
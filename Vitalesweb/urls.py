from django.urls import path
from . import views

app_name = 'vitalesweb'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('nosotros/', views.nosotros_view, name='nosotros'),
    path('servicios/', views.servicios_view, name='servicios'),
    path('contacto/', views.contacto_redirect, name='contacto'),
]

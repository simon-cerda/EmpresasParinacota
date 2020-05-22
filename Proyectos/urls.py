from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('Obras', views.obras_list, name="obras_list"),
    path('Agregar', views.form_view, name="form_view"),
    path('Obra/<int:id>/', views.detalle_obra, name="detalle_obra"),
]


from readline import append_history_file
from django.urls import URLPattern, path
from rango import views

app_name = 'rango'

URLPattern = [
    path('', views.index, name = 'index'),
]
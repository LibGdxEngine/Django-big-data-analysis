from django.urls import path
from .views import plate_graphs_view

app_name = 'plates'

urlpatterns = [
    path('', plate_graphs_view, name="main-plates-view"),
]


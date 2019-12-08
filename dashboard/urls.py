from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('map/', views.map, name='map'),
]

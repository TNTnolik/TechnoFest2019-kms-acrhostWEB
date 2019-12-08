from django.urls import path
from rest_framework.authtoken import views as avi
from . import views

urlpatterns = [
    path('auth/', avi.obtain_auth_token),
    path('mind/create', views.MindCreateView.as_view()),
    path('cell/create', views.CellCreateView.as_view()),
    path('arrow/create', views.ArrowCreateView.as_view()),
    path('arrow/list', views.ArrowListView.as_view()),
]
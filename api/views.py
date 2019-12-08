from django.shortcuts import render
from rest_framework import generics
from .serializers import *

class MindCreateView(generics.CreateAPIView):
	serializer_class = MindDetailSerializer

class CellCreateView(generics.CreateAPIView):
	serializer_class = CellDetailSerializer

class ArrowCreateView(generics.CreateAPIView):
	serializer_class = ArrowDetailSerializer

class ArrowListView(generics.ListAPIView):
	serializer_class = ArrowDetailSerializer
	queryset = arrow.objects.all()
from django.shortcuts import render
from rest_framework import viewsets
from .models import developer, console, game
from .serializers import developer_serializer, console_serializer, game_serializer

# Create your views here.

class developer_viewset(viewsets.ModelViewSet):
    serializer_class = developer_serializer
    queryset = developer.objects.all()

class console_viewset(viewsets.ModelViewSet):
    serializer_class = console_serializer
    queryset = console.objects.all()

class game_viewset(viewsets.ModelViewSet):
    serializer_class = game_serializer
    queryset = game.objects.all()
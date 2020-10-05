from rest_framework import serializers
from .models import developer, console, game

class developer_serializer(serializers.ModelSerializer):
    class Meta:
        model = developer
        fields = '__all__'

class console_serializer(serializers.ModelSerializer):
    class Meta:
        model = console
        fields = '__all__'

class game_serializer(serializers.ModelSerializer):
    class Meta:
        model = game
        fields = '__all__'
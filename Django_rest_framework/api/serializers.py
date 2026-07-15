from rest_framework import serializers

class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    cuisine = serializers.CharField(max_length=100)

# Prompt used to generate this code (using Copilot/ChatGPT):
# "Write a basic Django REST Framework Serializer class for a Zomato-style Restaurant object with fields: name and cuisine."

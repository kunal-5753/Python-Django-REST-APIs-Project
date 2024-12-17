from rest_framework import serializers
from .models import Client, Project, User

# Serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_at', 'created_by', 'client', 'user']

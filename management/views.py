from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from .models import Client, Project, User
from .serializers import ClientSerializer, ProjectSerializer, UserSerializer

# Create your views here.

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientFunction(APIView):
    def get(self, request, id):
        try:
            client = Client.objects.get(id=id)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except Client.DoesNotExist:
            return Response({"Client not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
    def put(self, request, id):
        try:
            client = Client.objects.get(id=id)
        except Client.DoesNotExist:
            return Response({"Client not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClientSerializer(client, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, id):
        try:
            client = Client.objects.get(id=id)
        except Client.DoesNotExist:
            return Response({"Client not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            client = Client.objects.get(id=id)
            client.delete()
            return Response({"detail": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response({"detail": "Client not found"}, status=status.HTTP_404_NOT_FOUND)



class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectCreate(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

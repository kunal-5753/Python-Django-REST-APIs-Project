from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)


class Client(models.Model):
    client_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
 

class Project(models.Model):
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)

from django.urls import path
from .views import ClientCreate, ClientFunction, ClientList, ProjectCreate, ProjectList, UserCreate, UserList

urlpatterns = [
    path('user/create/', UserCreate.as_view(), name='user-create'),
    path('user/list/', UserList.as_view(), name='user-list'),
    path('client/create/', ClientCreate.as_view(), name='client-create'),
    path('client/list/', ClientList.as_view(), name='client-list'),
    path('client/<int:id>/', ClientFunction.as_view(), name='client-functions'),
    path('project/create/', ProjectCreate.as_view(), name='project-create'),
    path('project/list/', ProjectList.as_view(), name='project-list'),
]

from rest_framework import viewsets
from app.serializers import ToDoSerializers
from app.models import ToDo

# Create your views here. ONDE ESTÁ A NOSSA LÓGICA

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers
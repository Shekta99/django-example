from rest_framework import viewsets
from rest.models import Tarea
from rest.serializers import TareaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    
    @action(detail=False, methods=['GET'])
    def completadas(self, request):
        return Response('hola')
    

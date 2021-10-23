from rest_framework import viewsets
from .serializers import *
from .models import *

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class InfoPessoalViewSet(viewsets.ModelViewSet):
    queryset = Informacao_Pessoal.objects.all()
    serializer_class = InfoPessoalSerializer
    
class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
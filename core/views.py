from rest_framework import viewsets, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.db import transaction
from django_filters import rest_framework as filters


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id','id_medico','id_paciente','status','data','hora')

    def create(self, request,*args, **kwargs):
        try:
            with transaction.atomic():
                data = request.data.get("data"),
                hora = request.data.get("hora"),
                data_hora = data[0] + 'T' + hora[0],
                agendamento = Agendamento.objects.create(
                    id_medico_id=request.data.get("id_medico"),
                    id_paciente_id=request.data.get("id_paciente"),
                    status = request.data.get("status"),
                    data = request.data.get("data"),
                    hora = request.data.get("hora"),
                    data_hora = data_hora[0],
                )
                print("consegui criar: ",agendamento)
                agendamento.save()

                return Response()

        except Exception as exception:
            print("Erro: ",exception)
            result = {  
                "agendamento": "Esse horário já está ocupado para esse dia."
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)


class InfoPessoalViewSet(viewsets.ModelViewSet):
    queryset = Informacao_Pessoal.objects.all()
    serializer_class = InfoPessoalSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id','id_paciente')
    
class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id','id_paciente','id_medico')
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .serializers import *
from .models import *
from authapi.models import *
from rest_framework.response import Response
from django.db import transaction
from django_filters import rest_framework as filters
import datetime


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id','id_medico','id_paciente','status','data','hora','data_hora')

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
                result = {
                    "agendamento":"Criado com sucesso."
                }
                return Response(result, status=status.HTTP_201_CREATED)

        except Exception as exception:
            print("Erro: ",exception)
            result = {  
                "agendamento": "Esse horário já está ocupado para esse dia."
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

class AgendamentoChangeStatusViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoStatusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id','id_paciente', 'id_medico')


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

class RelatoriosViewSet(APIView):
    def post(self, request, format=None):
        """
        Check which report is requested:
        """
        id = request.data.get("id")
        if id == '1':
            infos_pessoais_array = Informacao_Pessoal.objects.all()
            dob_array = []
            age_array = []
            for person in infos_pessoais_array:
                dob_array.append(person.data_nascimento)
                age_array.append(from_dob_to_age(person.data_nascimento))
            age_array.sort()
            dob_array.sort()
            result = {
                "total_registered:":infos_pessoais_array.__len__(),
                "oldest_name:":Informacao_Pessoal.objects.filter(data_nascimento=dob_array[0])[0].nome_completo,
                "oldest_age:":age_array[age_array.__len__()-1],
                "youngest_name:":Informacao_Pessoal.objects.filter(data_nascimento=dob_array[dob_array.__len__()-1])[0].nome_completo,
                "youngest_age:":age_array[0],
                "average_age":sum(age_array) / len(age_array)
            }
            return Response(result,status=status.HTTP_200_OK)
        elif id == '2':
            result={}
            return Response(result,status=status.HTTP_200_OK)
        elif id == '3':
            infos_pessoais_array = Informacao_Pessoal.objects.all()
            agendamentos_array = []
            for person in infos_pessoais_array:
                agendamentos_array.append({
                    "name":person.nome_completo,
                    "qnt":Agendamento.objects.filter(id_paciente=person.id_paciente_id).__len__()
                })
            numero_agendamentos = 0
            nome_pessoa = "Nobody"
            for person in agendamentos_array:
                print(person)
                if person['qnt'] > numero_agendamentos:
                    numero_agendamentos = person['qnt']
                    nome_pessoa = person['nome_completo']
            result={
                "name":nome_pessoa,
                "qnt":numero_agendamentos
            }
            return Response(result,status=status.HTTP_200_OK)
        elif id == '4':
            agendamentos_array = Agendamento.objects.all()
            count_ended = 0
            count_canceled = 0
            count_awaiting = 0
            count_confirmed = 0
            for agendamento in agendamentos_array:
                if(agendamento.status == 0):
                    count_awaiting = count_awaiting + 1
                elif(agendamento.status == 1):
                    count_confirmed = count_confirmed + 1
                elif(agendamento.status == 2):
                    count_canceled = count_canceled + 1
                elif(agendamento.status == 3):
                    count_ended = count_ended + 1
            result={
                "total":agendamentos_array.__len__(),
                "ended": count_ended,
                "canceled": count_canceled,
                "awaiting": count_awaiting,
                "confirmed": count_confirmed
            }
            return Response(result,status=status.HTTP_200_OK)
        else:
            return Response("Relatório não encontrado",status=status.HTTP_400_BAD_REQUEST)

def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
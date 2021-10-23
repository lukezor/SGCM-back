from rest_framework import serializers
from .models import Agendamento, Informacao_Pessoal, Prontuario

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

class InfoPessoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informacao_Pessoal
        fields = '__all__'

class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario
        fields = '__all__'
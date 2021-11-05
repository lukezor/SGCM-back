from django.db import models
from authapi.models import User
from django.utils import timezone

# Create your models here.
class Informacao_Pessoal(models.Model):
    SEXOS = ( 
        ("M", "Masculino"),
        ("F","Feminino")
    )
    id_paciente = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    profissao = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXOS)
    documento = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    cor_raca = models.CharField(max_length=20)
    naturalidade = models.CharField(max_length=50)
    religiao = models.CharField(max_length=50, null=True)
    estado_civil = models.CharField(max_length=50)
    reponsavel = models.CharField(max_length=50, null=True)
    plano_saude = models.CharField(max_length=50, null=True)
    data_cadastro = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome_completo

class Agendamento(models.Model):
    AGENDAMENTO_STATUS = (
        (0, "Aguardando Confirmação"),
        (1, "Confirmado"),
        (2, "Cancelado"),
        (3, "Finalizado")
    )
    id_paciente = models.ForeignKey(User, related_name="id_paciente_atendimento", on_delete=models.CASCADE)
    id_medico = models.ForeignKey(User, related_name="id_medico_atendimento",on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    data_hora = models.CharField(max_length=20)
    status = models.IntegerField(choices=AGENDAMENTO_STATUS)

    def __str__(self):
        return self.data_hora + " - " + self.status

    class Meta:
        unique_together = [['id_medico', 'data_hora'],['id_paciente', 'data_hora']]

class Prontuario(models.Model):
    id_paciente = models.ForeignKey(User, related_name="id_paciente_prontuario", on_delete=models.CASCADE)
    id_medico = models.ForeignKey(User, related_name="id_medico_prontuario",on_delete=models.CASCADE)
    ref = models.CharField(max_length=200,default=timezone.localtime(timezone.now()).date())
    qd = models.TextField()
    hda = models.TextField()
    efg = models.TextField()
    habitos = models.TextField()
    antecedentes_pessoais = models.TextField()
    antecedentes_familiares = models.TextField()
    hipotese_cid = models.TextField()
    conduta = models.TextField()
    exames = models.TextField()
    receitas = models.TextField()
    evolucoes = models.TextField()
    info_adicional = models.TextField()

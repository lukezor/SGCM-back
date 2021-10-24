from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    TIPOS_USUARIO = (
        ("ADMIN", "Administrador"),
        ("SECRETARIO", "Secretário"),
        ("PACIENTE", "Paciente"),
        ("MEDICO", "Medico")
    )
    user_type = models.CharField(choices=TIPOS_USUARIO, max_length=15)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    date_joined = models.DateField(auto_now=True)
    info_cadastrada = models.BooleanField(null=True,blank=True)

    REQUIRED_FIELDS = ['email','user_type','first_name','last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_username(self):
        return self.username

# Create your models here.

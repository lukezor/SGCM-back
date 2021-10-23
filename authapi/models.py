from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    TIPOS_USUARIO = (
        (0, "Administrador"),
        (1, "Secretário"),
        (2, "Paciente"),
        (3, "Medico")
    )
    user_type = models.IntegerField(choices=TIPOS_USUARIO)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)

    REQUIRED_FIELDS = ['email','user_type','first_name','last_name']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def get_username(self):
        return self.username

# Create your models here.

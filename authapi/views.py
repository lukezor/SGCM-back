from rest_framework import viewsets
from .serializers import *
from .models import *
from django_filters import rest_framework as filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id','username','email','user_type','first_name','last_name','info_cadastrada','date_joined')
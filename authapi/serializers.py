from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','username','email','user_type','first_name','last_name','password','info_cadastrada','is_superuser','is_staff')

class UserViewSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id','username','email','user_type','first_name','last_name','date_joined','info_cadastrada')

class UserInfoSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id','info_cadastrada')
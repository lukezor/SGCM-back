from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from core.views import *
from authapi.views import *

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'userinfo',UserInfoViewSet)
router.register(r'agendamentos',AgendamentoViewSet)
router.register(r'infospessoais',InfoPessoalViewSet)
router.register(r'prontuarios',ProntuarioViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('authapi.urls')),
]
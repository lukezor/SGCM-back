from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('authapi.urls')),
]
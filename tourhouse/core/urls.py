from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.api.funcionario import FuncionarioViewSet
from core.api.sede import SedeViewSet
from core.api.departamento import DepartamentoViewSet

route = routers.DefaultRouter()
route.register('funcionario', FuncionarioViewSet, 'funcionario')
route.register('sede', SedeViewSet, 'sede')
route.register('departamento', DepartamentoViewSet, 'departamento')


urlpatterns = [
    path('api/', include(route.urls), name='api'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token/refresh'),
    
]
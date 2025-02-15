from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .auth import (
    UserAuthViewSet
)

from .views import (
    UserViewSet,
    CategoriaViewSet,
    CuentaViewSet,
    PresupuestoViewSet,
    TransaccionViewSet,
)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'cuentas', CuentaViewSet)
router.register(r'presupuestos', PresupuestoViewSet)
router.register(r'transacciones', TransaccionViewSet)
router.register(r'auth', UserAuthViewSet, basename='auth')
router.register(r'cuenta', UserViewSet, basename='account')

urlpatterns = [
    path('Finance/', include(router.urls)),
]

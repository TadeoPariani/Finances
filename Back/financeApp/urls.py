from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
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

urlpatterns = [
    path('', include(router.urls)),
]

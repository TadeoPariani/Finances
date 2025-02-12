from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransaccionViewSet

router = DefaultRouter()
router.register(r'transacciones', TransaccionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

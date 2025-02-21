from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Categoria, Cuenta, Presupuesto, Transaccion

from .serializers import (
    UserSerializer, 
    CategoriaSerializer, 
    CuentaSerializer, 
    PresupuestoSerializer, 
    TransaccionSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #sobreescribe el metodo del ViewSet
        return User.objects.filter(id=self.request.user.id)  #Limita las acciones a su propio Usuario
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Actualiza lo que necesites sin tener que usar PATCH
        serializer.is_valid(raise_exception=True)

        print("USERVIEWSET:", type(instance))

        if instance.id != request.user.id: #QUEDA COMO UN SEGURO
            return Response({"ERROR DE AUTENTICACION"}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_update(serializer)
        return Response({"Se actualizo el usuario": serializer.data})
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        if instance.id != request.user.id: #QUEDA COMO UN SEGURO
            return Response({"ERROR DE AUTENTICACION"}, status=status.HTTP_403_FORBIDDEN)
        
        self.perform_destroy(instance)
        return Response({"deleted_user": serializer.data}, status=status.HTTP_204_NO_CONTENT)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class PresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    queryset = Transaccion.objects.all()
    serializer_class = TransaccionSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder



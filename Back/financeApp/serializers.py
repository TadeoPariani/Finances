from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Categoria, Cuenta, Presupuesto, Transaccion

class UserSerializer(serializers.ModelSerializer): #REVISAR ETO
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField(required=True)
    last_login = serializers.CharField(write_only=True, required=False)
    is_superuser = serializers.CharField(write_only=True, required=False)
    is_staff = serializers.CharField(write_only=True, required=False)
    is_active = serializers.CharField(write_only=True, required=False)
    date_joined = serializers.CharField(write_only=True, required=False)
    groups = serializers.CharField(write_only=True, required=False)
    user_permissions = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data: #para que no se rompa si password no esta en la query, pero que si esta la hashea
            validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).update(instance, validated_data)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class PresupuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presupuesto
        fields = '__all__'

class TransaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = '__all__'


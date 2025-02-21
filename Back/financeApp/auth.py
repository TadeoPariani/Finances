from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from.serializers import UserSerializer

# UNICAMENTE PARA AUTH
class UserAuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Usuario Creado Exitosamente", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            csrf_token = get_token(request)  # Generar el token CSRF
            return Response(
                    {
                        "message": "Login exitoso",
                        "csrfToken": csrf_token,
                        "user": UserSerializer(user).data  # Devuelve los datos serializados del usuario
                    },
                    status=status.HTTP_200_OK
            )
        else:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        if request.user.is_authenticated:
                logout(request)
                return Response({"message": "Logout exitoso"}, status=status.HTTP_200_OK)
        return Response({"error": "No hay usuario autenticado"}, status=status.HTTP_400_BAD_REQUEST)
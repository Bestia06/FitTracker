# user/api_views.py
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from .serializers import UserSerializer, UserCreateSerializer, LoginSerializer

@extend_schema(
    tags=['auth'],
    summary="Registrar nuevo usuario",
    description="Crea un nuevo usuario en el sistema",
    examples=[
        OpenApiExample(
            'Ejemplo de registro',
            value={
                'username': 'nuevo_usuario',
                'email': 'usuario@example.com',
                'password': 'password123',
                'first_name': 'Juan',
                'last_name': 'Pérez'
            }
        )
    ]
)
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """Registrar nuevo usuario"""
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'Usuario creado exitosamente'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """Login de usuario"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'Login exitoso'
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile(request):
    """Obtener perfil del usuario autenticado"""
    return Response(UserSerializer(request.user).data)
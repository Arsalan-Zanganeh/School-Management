from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Profile, User
from .serializer import UserSerializer, MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ([AllowAny])
    serializer_class = RegisterSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':
        response = f"Hey {request.user}, You are seeing a GET response"
        return Response({'response': response}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get['text']
        response = f"Hey {request.user}, You are seeing a POST response"
        return Response({'response': response}, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)



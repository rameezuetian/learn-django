from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsOwnerOrModeratorOrAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrModeratorOrAdmin]
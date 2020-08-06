from django.contrib.auth.models import User
from djangoapp.models import Musician
from rest_framework import viewsets
from rest_framework import permissions
from urls import UserSerializer, MusicianSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MusicianViewSet(viewsets.ModelViewSet):
    """API endpoint that allows musicians to be viewed or edited."""

    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    permission_classes = [permissions.IsAuthenticated]

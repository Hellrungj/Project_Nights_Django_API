from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from .models import Event, Guest, Type
from rest_framework import viewsets
from api.quickstart.serializers import UserSerializer, GroupSerializer, EventSerializer, GuestSerializer, TypeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GuestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
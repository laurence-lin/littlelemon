from django.shortcuts import render
from django.http import HttpResponse, response
from django.contrib.auth.models import User, Group
from rest_framework import generics, viewsets, permissions
from .serializers import MenuItemSerializer, MenuSerializer
from .models import MenuItem, Menu
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class MenuItemView(generics.ListCreateAPIView):
    permission_classes = []
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer




@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
#    return "Protected!"
    return HttpResponse({"message":"This view is protected"})
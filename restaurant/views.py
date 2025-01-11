from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import generics, viewsets, permissions
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .models import Menu, Booking


# Create your views here.


def home(request):
    return HttpResponse("Home page of Restaurant APP")



def index(request):
    return render(request, 'index.html', {})



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #permission_classes = [] # Override DEFAULT_AUTHENTICATION_CLASS that requires token
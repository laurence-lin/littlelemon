from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MenuItem, Menu



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
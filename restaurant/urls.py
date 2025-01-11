from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter() # DefaultRouter contains all RESTful methods for Viewsets
router.register(r'users', views.UserViewSet) # Register the View to users URL
router.register(r'booking/tables', views.BookingViewSet)

urlpatterns = [
    path('index/', views.index, name="index"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemView.as_view()),
]
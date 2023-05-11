from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('', views.usuarios_view, name='usuario_view'),
    path('<int:pk>', views.usuario_view, name='usuario_login'),
    path('usuarioCreate/', csrf_exempt(views.create_usuario), name='usuarioCreate'),
]


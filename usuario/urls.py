from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_usuarios, name='usuarios_view'),
    path('<int:pk>', views.get_usuario_by_pk, name='get_usuario_by_pk'),
     path('usuario_view/<str:pk>/', views.get_usuario_by_correo, name='get_usuario_by_correo'),
    path('usuarioCreate/', views.create_usuario, name='usuario_create'),
]


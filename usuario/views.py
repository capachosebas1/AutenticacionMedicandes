from django.shortcuts import render
from .logic import usuario_logic as ul
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from .forms import UsuarioForm
from .logic.usuario_logic import create_usuario
from django.contrib.auth.decorators import login_required
#from autenticacion.auth0backend import getRole

@csrf_exempt
def usuario_view(request, pk):
    if request.method == 'GET':
        usuario_dto = ul.get_usuario(pk)
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')

    if request.method == 'PUT':
        data = json.loads(request.body)
        rol = data.get("rol")
 
        usuario_dto = ul.update_usuario(pk, rol)
        usuario = serializers.serialize('json', [usuario,])
        return HttpResponse(usuario, 'application/json')

def usuarios_view(request):

    if request.method == 'GET':
        usuario_dto = ul.get_usuarios()
        usuarios = serializers.serialize('json', usuario_dto,)
        return HttpResponse(usuarios, 'application/json')


@csrf_exempt
def usuario_view(request):
    
    if request.method == 'POST':
        usuario_dto = ul.create_usuario(json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')
        
        
#@login_required
def usuario_create(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            create_usuario(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created Usuario')
            return HttpResponseRedirect(reverse('usuarioCreate'))
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    context = {
        'form': form,
    }
    return render(request, 'Usuario/usuarioCreate.html', context)


from ..models import Usuario

def get_usuario(correo):
    usuario = Usuario.objects.get(pk=correo)
    return usuario

def get_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def create_usuario(hist, form):
    usuario = Usuario(name=hist["correo"])
    usuario = form.save()
    usuario.save()
    return usuario

def update_usuario(correo, rol):
    usuario = get_usuario(correo)
    usuario.rol = rol["rol"]

    usuario.save()
    return usuario
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones
from cafe.forms import *
from cafe.models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from register.forms import RegistroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    print(lista)
    if len(lista)!=0:
        imagen="/" + lista[0].imagen.url
    else:
        imagen="/media/avatarpordefecto.png"
    return imagen


@login_required
def inicio(request):
    
    return render (request, "cafe/inicio.html", {"imagen":obtenerAvatar(request)})
    

@login_required
def About(request):
      return render (request, "cafe/about.html", {"imagen":obtenerAvatar(request)})


@login_required
def blog(request):
      return render (request, "cafe/blog.html", {"imagen":obtenerAvatar(request)})

@login_required
def ups(request):
      return render (request, "cafe/ups.html", {"imagen":obtenerAvatar(request)})

@ login_required
def profile(request):
    profile = Perfil.objects.all()
    if profile:
        descripcion = profile[0].descripcion
        link = profile[0].link
    else:
        descripcion = ""
        link = ""
    return render(request, "cafe/profile.html", {"descripcion" : descripcion, "link": link})

@login_required
def editarContrasena(request):
    if request.method == "POST":
        formulario = PasswordChangeForm(data = request.POST, user = request.user)
        if formulario.is_valid():
            formulario.save()
            update_session_auth_hash(request, formulario.user)
            return render(request, "cafe/profile.html", {"mensaje_utilidad": f"La contraseña ha sido editada!", "imagen": obtenerAvatar(request)})
        else:
           return render(request, "cafe/editarContrasena.html", {"form_edit_user" : PasswordChangeForm(user = request.user), "mensaje_registro": "Intentelo Nuevamente, hubo un error", "imagen": obtenerAvatar(request)})
    else:
        return render(request, "cafe/editarContrasena.html", {"form_edit_user": PasswordChangeForm(user = request.user), "mensaje_registro":"Editar contraseña", "imagen": obtenerAvatar(request)})

@ login_required
def editarProfile(request):
    
    datos_viejos = Perfil.objects.all()
    if datos_viejos:
        formulario_edit = UserEditForm(initial={"descripcion": datos_viejos[0].descripcion, "link": datos_viejos[0].link})
    else:
        formulario_edit = UserEditForm()
    if request.method == "POST":
        formulario = PerfilForm(request.POST, request.FILES)
        if formulario.is_valid():
            datos_viejos = Perfil.objects.all()
            if datos_viejos != None:        
                datos_viejos.delete()

            datos_nuevos = Perfil(descripcion = request.POST["descripcion"], link = request.POST["link"])
            datos_nuevos.save()
            return render(request, "cafe/profile.html", {"mensaje_utilidad": "El perfil ha sido editado exitosamente!", "imagen": obtenerAvatar(request)})
        else:
            return render(request, "cafe/editarProfile.html", {"form_edit_profile" : formulario_edit, "mensaje_registro": "Intentelo Nuevamente, hubo un error", "imagen": obtenerAvatar(request)})
    else:
        return render(request, "cafe/editarProfile.html", {"form_edit_profile": formulario_edit, "mensaje_registro":"Editar perfil", "imagen": obtenerAvatar(request)}) 


@login_required
def blog(request):

    if request.method=="POST":
        form=BlogForm(request.POST)
        formulario=BlogForm()

        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            titulo=informacion["titulo"]
            subtitulo=informacion["subtitulo"]
            cuerpo=informacion["cuerpo"]
            autor=informacion["autor"]
            fecha=informacion["fecha"]
            imagen=informacion["imagen"]
            blog=Blog(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor,fecha=fecha, imagen=imagen)
            blog.save()
            return render (request, "cafe/blog.html", {"mensaje": "BLOG CREADO"})
    else:
        formulario=BlogForm()


    return render (request, "cafe/blog.html", {"form":formulario})


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request,"cafe/inicio.html", {"mensaje":"Avatar agregado correctamente"})
        else:
            return render(request, "cafe/agregarAvatar.html", {"formulario": form, "usuario":request.user})
    else:
        form=AvatarForm()
        return render(request, "cafe/agregarAvatar.html", {"formulario": form, "usuario":request.user})

def pages(request):
      pages=Blog.objects.all()
      print(pages)
      return render(request, "cafe/pages.html", {"blog":pages})

from django.urls import path
from cafe.views import *
from cafe.models import*

urlpatterns = [
    path("home/", inicio, name="inicio"),
    path("about/", About, name="about"),
    path("blog/", blog, name="blog"),
    path("accounts/profile/", profile, name="profile"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("pages/[id_post]", pages, name="pages"),
    path("ups/", ups, name="ups"),
    path("editarProfile/", editarProfile, name="editarProfile"),
    path("editarContrasena/", editarContrasena, name="editarContrasena"),
    path("pages/pageId/", pages, name="pageId"),
]
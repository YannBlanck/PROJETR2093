from django.shortcuts import render
from .forms import AlbumsForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'album/index.html')

def ajout(request):
    form = AlbumsForm()
    return render(request, "album/ajout.html", {"form": form})

def traitement(request):
    lform = AlbumsForm(request.POST)
    if lform.is_valid():
        albums = lform.save()
        return HttpResponseRedirect('/album/')
    else:
        return render(request,"album/ajout.html",{"form": lform})

def affiche(request, id):
    albumss = models.Albums.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"album/affiche.html",{"albums": albumss})

def index(request):
    liste = list(models.Albums.objects.all())
    return render(request,'album/index.html',{'liste': liste})

def update(request, id):
    liste = models.Albums.objects.get(pk=id)
    form = AlbumsForm(liste.music())
    return render(request, "album/ajout.html", {"form":form})

def updatetraitement(request, id):
    lform = AlbumsForm(request.POST)
    if lform.is_valid():
        upalbums = lform.save(commit= False)
        upalbums.id = id
        upalbums.save()
        return HttpResponseRedirect('/album/')
    else:
        return render(request,"album/ajout.html",{"form": lform, "id": id} )

def delete(request, id ):
    dalbum = models.Albums.objects.get(pk=id)
    dalbum.delete()
    return HttpResponseRedirect('/album')
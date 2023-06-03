from django.shortcuts import render
from .forms import AcheterForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.
def acheterindex(request):
    return render(request, 'Acheter/index.html')

def acheterajout(request):
    form = AcheterForm()
    return render(request, "Acheter/ajout.html", {"form": form, "id":id})

def achetertraitement(request):
    lform = AcheterForm(request.POST)
    if lform.is_valid():
        acheter = lform.save()
        return HttpResponseRedirect('/album/')
    else:
        return render(request,"Acheter/ajout.html",{"form": lform})

def acheteraffiche(request, id):
    acheterr = models.Acheter.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"Acheter/affiche.html",{"acheter": acheterr})

def acheterindex(request):
    liste = list(models.Acheter.objects.all())
    return render(request,'Acheter/index.html',{'liste': liste})

def acheterupdate(request, id):
    liste = models.Acheter.objects.get(pk=id)
    form = AcheterForm(liste.ach())
    return render(request, "Acheter/ajout.html", {"form":form})

def acheterupdatetraitement(request, id):
    lform = AcheterForm(request.POST)
    if lform.is_valid():
        upachat = lform.save(commit= False)
        upachat.id = id
        upachat.save()
        return HttpResponseRedirect('/album/')
    else:
        return render(request,"Acheter/ajout.html",{"form": lform, "id": id} )

def acheterdelete(request, id ):
    dachat = models.Acheter.objects.get(pk=id)
    dachat.delete()
    return HttpResponseRedirect('/album')
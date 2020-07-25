from django.shortcuts import render

# Create your views here.
def Inicio (request):
    return render(request,"index.html")

def Nosotros (request):
    return render(request,"nosotros.html")

def Contacto  (request):
    return render(request,"contacto.html")

def Servicio  (request):
    return render(request,"servicios.html")
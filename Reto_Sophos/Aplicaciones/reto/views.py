from django.shortcuts import render, redirect
from .models import Heroe,Villano,Pelea, Patrocinador
from django.db.models import Q

#HEROE

def home(request):
    heroes = Heroe.objects.all()  
    return render(request, "gestionHeroes.html", {"heroes": heroes})

def crearHeroe(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        edad = request.POST['txtEdad']
        origen = request.POST['txtOrigen']
        habilidades = request.POST['txtHabilidades']
        debilidad = request.POST['txtDebilidad']

        # Buscar el último ID de Heroe y agregar 1
        idPasado = Heroe.objects.order_by('-id_heroe').first()
        nuevoid_heroe = 1 if idPasado is None else idPasado.id_heroe + 1

        heroe = Heroe(id_heroe=nuevoid_heroe, nombre=nombre, edad=edad, origen=origen, habilidades=habilidades, debilidad=debilidad)
        heroe.save()

        return redirect('/')

def editarHeroe(request, id_heroe):
    if request.method == 'POST':
        nombre = request.POST['editNombre']
        edad = request.POST['editEdad']
        origen = request.POST['editOrigen']
        habilidades = request.POST['editHabilidades']
        debilidad = request.POST['editDebilidad']

        heroe = Heroe.objects.get(id_heroe=id_heroe)
        heroe.nombre = nombre
        heroe.edad = edad
        heroe.origen = origen
        heroe.habilidades = habilidades
        heroe.debilidad = debilidad
        heroe.save()

    return redirect('/')

def eliminarHeroe(request,id_heroe):
    heroe = Heroe.objects.get(id_heroe=id_heroe)
    heroe.delete()
    return redirect('/')

def buscarHeroe(request):
    resultados_busqueda = []

    if 'q' in request.GET:
        query = request.GET['q']
        resultados_nombre = Heroe.objects.filter(nombre__icontains=query)
        resultados_habilidades = Heroe.objects.filter(habilidades__icontains=query)
        resultados_busqueda = list(resultados_nombre.values() | resultados_habilidades.values())
    else:
        resultados_busqueda = list(Heroe.objects.all().values())

    return render(request, 'gestionHeroes.html', {'resultados_busqueda': resultados_busqueda})

#VILLANOS 

def gestion_villanos(request):
    villanos = Villano.objects.all()
    return render(request, "gestionVillanos.html", {"villanos": villanos})

def crearVillano(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        edad = request.POST['txtEdad']
        origen = request.POST['txtOrigen']
        habilidades = request.POST['txtHabilidades']
        debilidad = request.POST['txtDebilidad']

        idPasado = Villano.objects.order_by('-id_villano').first()
        nuevoId_villano = 1 if idPasado is None else idPasado.id_villano + 1
    

        villano = Villano(id_villano=nuevoId_villano, nombre=nombre, edad=edad, origen=origen, habilidades=habilidades, debilidad=debilidad)
        villano.save()

        return redirect('gestion_villanos')

def editarVillano(request, id_villano):
    if request.method == 'POST':
        nombre = request.POST['editNombre']
        edad = request.POST['editEdad']
        origen = request.POST['editOrigen']
        habilidades = request.POST['editHabilidades']
        debilidad = request.POST['editDebilidad']

        villano = Villano.objects.get(id_villano=id_villano)
        villano.nombre = nombre
        villano.edad = edad
        villano.origen = origen
        villano.habilidades = habilidades
        villano.debilidad = debilidad
        villano.save()

    return redirect('gestion_villanos')

def eliminarVillano(request,id_villano):
    villano = Villano.objects.get(id_villano=id_villano)
    villano.delete()
    return redirect('gestion_villanos')

def buscarVillano(request):
    resultados_busqueda = []

    if 'q' in request.GET:
        query = request.GET['q']
        resultados_nombre = Villano.objects.filter(nombre__icontains=query)
        resultados_habilidades = Villano.objects.filter(habilidades__icontains=query)
        resultados_origen = Villano.objects.filter(origen__icontains=query)
        resultados_debilidad = Villano.objects.filter(debilidad__icontains=query)
        resultados_busqueda = list(resultados_nombre.values() | resultados_habilidades.values() | resultados_origen.values() | resultados_debilidad.values())
        
    else:
        resultados_busqueda = list(Villano.objects.all().values())

    return render(request, 'gestionVillanos.html', {'resultados_busqueda': resultados_busqueda})

#PELEAS

def gestion_pelea(request):
    peleas = Pelea.objects.all()
    return render(request, "gestionPeleas.html", {"pelea": peleas})

def crearPelea(request):
    if request.method == 'POST':
        id_villano = request.POST.get('txtVillano')
        id_heroe = request.POST.get('txtHeroe')
        resultado = request.POST.get('txtResultado')
        
        
        idPasado = Pelea.objects.order_by('-id_pelea').first()
        nuevoId_pelea = 1 if idPasado is None else idPasado.id_pelea + 1

        villano = Villano.objects.get(pk=id_villano)
        heroe = Heroe.objects.get(pk=id_heroe)
            
        pelea = Pelea(id_pelea=nuevoId_pelea, id_villano=villano, id_heroe=heroe, resultado=resultado)
        pelea.save()

        return redirect('gestion_pelea')
    
def editarPelea(request, id_pelea):
    if request.method == 'POST':
        idHeroe = request.POST['editIdHeroe']
        idVillano = request.POST['editIdVillano']
        resultado = request.POST['editResultado']
        
        pelea = Pelea.objects.get(id_pelea=id_pelea)
        pelea.id_heroe = idHeroe
        pelea.id_villano = idVillano
        pelea.resultado = resultado
        pelea.save()

    return redirect('gestion_pelea')

def eliminarPelea(request, id_pelea):
    pelea = Pelea.objects.get(id_pelea=id_pelea)
    pelea.delete()
    return redirect('gestion_pelea')

def buscarPelea(request):
    resultados_busqueda = []

    if 'q' in request.GET:
        query = request.GET['q']
        resultados_busqueda = Pelea.objects.filter(
            Q(id_heroe__nombre__icontains=query) | Q(id_villano__nombre__icontains=query)
        )

    else:
        resultados_busqueda = Pelea.objects.all()

    return render(request, 'gestionPeleas.html', {'resultados_busqueda': resultados_busqueda})


#PATROCINADOR

def gestion_patrocinador(request):
    patrocinadores = Patrocinador.objects.all()
    return render(request, "gestionPatrocinador.html", {"patrocinador": patrocinadores})

def crearPatrocinador(request):
    if request.method == 'POST':

        nombre = request.POST['txtNombre']
        id_heroe = request.POST.get('txtHeroe')
        monto = request.POST.get('txtMonto')
        origenDinero = request.POST.get('txtOrigenDinero')
        
        idPasado = Patrocinador.objects.order_by('-id_patrocinador').first()
        nuevoId_patrocinador = 1 if idPasado is None else idPasado.id_patrocinador + 1

        heroe = Heroe.objects.get(pk=id_heroe)
            
        patrocinador = Patrocinador(id_patrocinador=nuevoId_patrocinador, nombre=nombre, id_heroe=heroe, monto=monto, origenDinero=origenDinero)
        patrocinador.save()

        return redirect('gestion_patrocinador')

def editarPatrocinador(request, id_patrocinador):
    if request.method == 'POST':
        nombre = request.POST['editNombre']
        idHeroe = request.POST['editIdHeroe']
        monto = request.POST['editMonto']
        origenDinero = request.POST['editOrigenDinero']


        patrocinador = Patrocinador.objects.get(id_patrocinador=id_patrocinador)
        patrocinador.id_heroe = idHeroe
        patrocinador.nombre = nombre
        patrocinador.monto= monto
        patrocinador.origenDinero = origenDinero
        patrocinador.save()

    return redirect('gestion_patrocinador')

def eliminarPatrocinador(request, id_patrocinador):
    patrocinador = Patrocinador.objects.get(id_patrocinador=id_patrocinador)
    patrocinador.delete()
    return redirect('gestion_patrocinador')

def buscarPatrocinador(request):
    resultados_busqueda = []

    if 'q' in request.GET:
        query = request.GET['q']
        resultados_busqueda = Patrocinador.objects.filter(
            Q(id_heroe__nombre__icontains=query) | Q(nombre__icontains=query)
        )

    else:
        resultados_busqueda = Patrocinador.objects.all()

    return render(request, 'gestionPatrocinador.html', {'resultados_busqueda': resultados_busqueda})
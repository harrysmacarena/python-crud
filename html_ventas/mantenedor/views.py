from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages 
from django.core import serializers
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
#https://hackersandslackers.com/creating-django-views/
from .models import Comuna,Persona,Provincia,Region
from django.forms.models import model_to_dict
#from rest_framework import serializers
from django.core import serializers

#from django.utils import simplejson

@csrf_exempt
def PersonaDelete(request):
    run= request.POST.get('run')
    persona = Persona.objects.get(pk=run)    
    persona.delete()
    return StreamingHttpResponse('{"ok":"true","msg":"Registro Eliminado"}')  

@csrf_exempt
def PersonaActualizar(request):
    run= request.POST.get('run')
    persona = Persona.objects.get(pk=run)    
    persona.nombres = request.POST.get('nombres')
    persona.apeMaterno = request.POST.get('apePaterno')
    persona.apeMaterno = request.POST.get('apeMaterno')
    persona.imagen = request.POST.get('imagen')
    persona.save()
    return StreamingHttpResponse('{"ok":"true","msg":"Registro Actualizado"}')  

@csrf_exempt
def PersonaLeer(request):
    print("Mis Post Persona",request.POST)
    runMaca = request.POST.get('runHarrys')
    persona = Persona.objects.filter(run=runMaca)
    #persona = Persona.objects.filter()
    #return StreamingHttpResponse('{"ok":"true","msg":"Si Probando Harrys Hermosa Houesten Persona Leer","claudio":"Claudio es un objeto"}')
    return StreamingHttpResponse(serializers.serialize("json", persona))   
    


@csrf_exempt
def ComunaDelete(request):
    idComuna =  request.POST.get('codigo')
    comuna = Comuna.objects.get(pk=idComuna)
    comuna.delete()
    print("Eliminando",comuna)
    #return StreamingHttpResponse(serializers.serialize("json", "comuna"))
    return StreamingHttpResponse('{"ok":"true","msg":"Registro Eliminado Harrys"}')

@csrf_exempt
def ComunaSave(request):
    idComuna =  request.POST.get('codigo')
    try:
        comuna = Comuna.objects.get(pk=idComuna)
        comuna.nombre_comuna=request.POST.get('descrip')
        comuna.stImagen=request.POST.get('imagen')
    except Comuna.DoesNotExist:
        comuna = Comuna( id_comuna = idComuna
                        ,nombre_comuna= request.POST.get('descrip')
                        ,stImagen= request.POST.get('imagen')
                        )
    comuna.save()
    #return StreamingHttpResponse(serializers.serialize("json", "comuna"))
    return StreamingHttpResponse('{"ok":"true","msg":"Registro actualizado Harrys"}')

@csrf_exempt
def ComunaLeer(request):
    #https://docs.djangoproject.com/en/3.1/topics/db/queries/
    #comuna = Comuna.objects.all()
    idComuna =  request.POST.get('codigo')
    comuna = Comuna.objects.filter(id_comuna=idComuna)
    #comuna = Comuna.objects.get(pk=5)
    #print("Mis comuna",comuna)
    #json_data = serializers.serialized("json", comuna )
    #json_data = JsonResponse(list(comuna), safe=False)
    #json_data = serializers.serialize('json', comuna)
    #return response
    #print(json.dumps(comuna))
    print(serializers.serialize("json", comuna))
    #if request.method == 'POST':
    #return StreamingHttpResponse(comuna.serialize())
    #print("type",type(list(comuna)))
    #return StreamingHttpResponse(JsonResponse(list(comuna), safe=False))
    #return JsonResponse({'results': list(comuna)})
    return StreamingHttpResponse(serializers.serialize("json", comuna))
    #return JsonResponse(model_to_dict(comuna), safe=False )
    #return render(request, 'mantenedor/comuna/index.html', {'ParRegistros': comuna})

@csrf_exempt
def ComunaFrm(request):
    if request.method == 'POST':
        idComuna =  request.POST.get('codigo')
        comuna = Comuna.objects.get(pk=idComuna)
    else :        
        comuna = Comuna( id_comuna = 1
                        ,nombre_comuna= 'X'
                        ,stImagen= 'Y'
                        )
    #provincia = Provincia.objects.filter(id=id)
    provincia = Provincia.objects.all()
    region = Region.objects.all()
    return render(request, 'mantenedor/Comuna/FrComuna.html'
           , {'ParRegistros': comuna
           ,'provinciaReg' : provincia
           ,'regionReg' : region
           }
        )
    #return render(request,"mantenedor/Comuna/FrComuna.html")
#**********************************************

def PersonaListado(request):
    persona = Persona.objects.all()
    print("Mis Registros",persona)
    return render(request, 'mantenedor/Persona/index.html', {'ParRegistros': persona})

@csrf_exempt    
def PersonaFrm(request):
    run =  request.POST.get('run')
    #print("Run",run)
    if run == "0":
        persona = None
    else:
        persona = Persona.objects.get(pk=run)

    region = Region.objects.all()
    #provincia = Provincia.objects.all()
    #comuna = Comuna.objects.all()
    #print("comuna", comuna)
    return render(request,"mantenedor/Persona/FrPersona.html"
                         ,{'regPersona': persona
                           ,'regRegion':region
                           #,'regProvincia':provincia
                           #,'regComuna':comuna
                           }
                )


##*************************************************

@csrf_exempt    
def ProvinciaCombo(request):
    idRegion =  request.POST.get('idRegion')
    provincia = Provincia.objects.filter(id_region=idRegion)
    return render(request,"mantenedor/Provincia/FrProvinciaCombo.html"
                         ,  {'regProvincia': provincia}
                )



##*************************************************
@csrf_exempt    
def ComunaCombo(request):
    idProvincia =  request.POST.get('idProvincia')
    comuna = Comuna.objects.filter(id_comuna=idProvincia)
    return render(request,"mantenedor/Comuna/FrComunaCombo.html"
                         ,  {'regComuna': comuna}
                )

def ComunaListado(request):
    comuna = Comuna.objects.all()
    print(comuna)
    return render(request, 'mantenedor/Comuna/index.html', {'comunaRegistros': comuna})
# Llamamos a la clase 'comuna' que se encuentra en nuestro archivo 'models.py'
class ComunaListado1(ListView): 
    model = Comuna 

class ComunaCrear(SuccessMessageMixin, CreateView): 
    model = Comuna # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Comuna # Definimos nuestro formulario con el nombre de la clase o modelo 'comuna'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Comuna' de nuestra Base de Datos 
    success_message = 'Comuna Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o comuna
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'    

class ComunaDetalle(DetailView): 
    model = Comuna # Llamamos a la clase 'Comuna' que se encuentra en nuestro archivo 'models.py'

class ComunaActualizar(SuccessMessageMixin, UpdateView): 
    model = Comuna # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Comuna # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Comuna Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class ComunaEliminar(SuccessMessageMixin, DeleteView): 
    model = Comuna 
    form = Comuna
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Comuna Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'        
##*************************************************



def index(request):
    return render(request,"mantenedor/index.html")

def producto(request):
    return render(request,"mantenedor/Productos/FrProducto.html")
def marca(request):
    return render(request,"mantenedor/Productos/FrMarca.html")
def modelo(request):
    return render(request,"mantenedor/Productos/FrModelo.html")
def bus(request):
    return render(request,"mantenedor/Productos/FrBus.html")    

def indexHarrys(request):
    return HttpResponse("Harrisito El Magnifico, Doble Magnifico")

def detail(request, preNro):
    return HttpResponse("You're looking at question SIiIII %s." % preNro)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detailError(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/detail.html', {'question': question})    
    return render(request, 'detail.html')    
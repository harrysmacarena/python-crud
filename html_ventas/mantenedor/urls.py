from django.contrib import admin
from django.urls import path
from . import views
from mantenedor.views import ComunaListado  , ComunaDetalle, ComunaCrear, ComunaActualizar, ComunaEliminar \
                      ,ComunaLeer \
                      ,PersonaListado,PersonaFrm

urlpatterns = [

##***********************************

    path('personaListado/', views.PersonaListado ,name='persona_list'),
    path('personaFrm/', views.PersonaFrm     ,name='persona_frm'),
    path('personaLeer', views.PersonaLeer     ,name='persona_leer'),
    path('personaActualizar', views.PersonaActualizar     ,name='persona_leer'),
    path('personaDelete', views.PersonaDelete     ,name='persona_leer'),

##***********************************
    # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    #path('comuna/', ComunaListado.as_view(template_name = "mantenedor/Comuna/index.html"), name='leer'),
    path('comunaListado/', views.ComunaListado ,name='comuna_list'),
    path('comunaLeer', views.ComunaLeer ,name='comuna_list'),
    path('comunaSave', views.ComunaSave ,name='comuna_save'),
    path('comunaDelete', views.ComunaDelete ,name='comuna_save'),
    path('comunaFrm/', views.ComunaFrm     ,name='comuna_frm'),
    path('comunaCombo/', views.ComunaCombo     ,name='comuna_combo'),

##***********************************

    #path('provinciaLeer', views.ProvinciaLeer ,name='provincia_leer'),
    path('provinciaCombo/', views.ProvinciaCombo     ,name='provincia_combo'),


    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('comuna/detalle/<int:pk>', ComunaDetalle.as_view(template_name = "mantenedor/comuna/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('comuna/crear', ComunaCrear.as_view(template_name = "mantenedor/comuna/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('comuna/editar/<int:pk>', ComunaActualizar.as_view(template_name = "mantenedor/comuna/actualizar.html"), name='actualizar'), 

    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('comuna/eliminar/<int:pk>', ComunaEliminar.as_view(), name='eliminar'),   

##***********************************

    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('polls/latest.html', views.indexHarrys),
    path('marca', views.marca),
    path('modelo', views.modelo),
    path('producto', views.producto),
    path('busxx', views.bus),

    path('error/<int:question_id>', views.detailError),


    # ex: /polls/5/
    path('<int:preNro>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),    
]

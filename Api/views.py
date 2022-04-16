from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.shortcuts import render
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import BaseUserManager
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from asyncio.windows_events import NULL

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authtoken.models import Token



from .helpers import errorMetodoNoPermitido, gestionarElementos, respuesta
from .models import  Diagnostico, Estudiante, Cliente, Entidad, Curso, ControlCalidad, InspeccionSupervicion, LevNorma, EstadoContrato, EstadoSolicitud,TipoDiagnostico, TipoContrato, TipoCurso, Tematica, TipoSolicitud,  TipoEntidad, Organismo, TipoServicio, TipoInstrumento, Magnitud, TipoInspeccion, TipoEspecialista, TipoNorma, Cargo, SectorEconomico, GestCertificado  
from .serializers import LogSerializer, UserSerializer, DiagnosticoSerializer,EstudianteSerializer, ClienteSerializer, ControlCalidadSerializer,CursoSerializer, EntidadSerializer,TipoDiagnosticoSerializer, InspeccionSupervicionSerializer, LevNormaSerializer, EstContratoSerializer, TipoInstrumento,  EstSolicitudSerializer, TipoContratoSerializer , TipoCursoSerializer, TipoSolicitudSerializer, TipoEntidadSerializer, OrganismoSerializer, TipoServicioSerializer, TipoInstrumentoSerializer, MagnitudSerializer, TipoInspeccionSerializer,TipoEspecialistaSerializer,TipoNormaSerializer, CargoSerializer, SectorEconomicoSerializer, GestCertificadoSerializer,TematicaSerializer

######### vistas para el modelo Diagnostico ############
# @csrf_exempt
# def gestionarDiagnostico(request, idAux = 0):
#         return gestionarElementos(request.method ,request,Diagnostico, DiagnosticoSerializer, idAux)

# ######### vistas para el modelo AdjuntarArchivo ############    
# @csrf_exempt
# def gestionarAdjuntarArchivo(request, idAux = 0):
#     return gestionarElementos(request.method ,request,AdjuntarArchivo, AdjuntarArchivoSerializer, idAux)

######### vistas para el modelo estudiante ############

#***************************************

@csrf_exempt
def trazas(request):
    if request.method == 'GET':
        logs = LogEntry.objects.all()
        return respuesta(LogSerializer(logs, many=True).data)
    else:
        return errorMetodoNoPermitido(request.method)

@csrf_exempt
def iniciarSesion(request):
    if request.method == "POST":
        datos = JSONParser().parse(request)
        username = datos['username']
        password = datos['password']
        acceso = authenticate(username=username, password=password)
        if acceso:
            login(request, acceso)
            usuario = User.objects.get(username = username)
            token, _ = Token.objects.get_or_create(user = usuario )
            return respuesta(token.key)
        return respuesta('Usuario o contraseña inconrrecta')

def cerrarSesion(request):
    logout(request)
    return respuesta(status=status.HTTP_200_OK)


@csrf_exempt
def gestionarUsuario(request, idAux=0):
    return gestionarElementos(request, User, UserSerializer, idAux)
    
@csrf_exempt
def gestionarEstudiante(request, idAux = 0):
    return gestionarElementos(request,Estudiante, EstudianteSerializer, idAux)

######### vistas para el modelo Cliente ############    
@csrf_exempt
def gestionarCliente(request, idAux = 0):
    return gestionarElementos(request,Cliente, ClienteSerializer, idAux)

######### vistas para el modelo ControlCalidad ############
@csrf_exempt
def gestionarControlCalidad(request, idAux = 0):
    return gestionarElementos(request,ControlCalidad, ControlCalidadSerializer, idAux)

######### vistas para el modelo Curso ############
@csrf_exempt
def gestionarCurso(request, idAux = 0):
    return gestionarElementos(request,Curso, CursoSerializer, idAux)

######### vistas para el modelo Entidad ############
@csrf_exempt
def gestionarEntidad(request, idAux = 0):
    return gestionarElementos(request,Entidad, EntidadSerializer, idAux)

######### vistas para el modelo inspección || supervició ############
@csrf_exempt
def gestionarInspeccionSupervicion(request, idAux = 0):
    return gestionarElementos(request,InspeccionSupervicion, InspeccionSupervicionSerializer, idAux)

######### vistas para el modelo inspección || supervició ############
@csrf_exempt
def gestionarLevNorma(request, idAux = 0):
    return gestionarElementos(request,LevNorma, LevNormaSerializer, idAux)

@csrf_exempt
def gestionarDiagnostico(request, idAux = 0):
    return gestionarElementos(request,Diagnostico, DiagnosticoSerializer, idAux)


#################### NOMENCLADORES #############################


######### vistas para el Nomenclador Estado Contrato ############
@csrf_exempt
def gestionarEstContrato(request, idAux = 0):
    return gestionarElementos(request,EstadoContrato, EstContratoSerializer, idAux)

######### vistas para el Nomenclador Tipo de Diagnostico ############
@csrf_exempt
def gestionarTipoDiagnostico(request, idAux = 0):
    return gestionarElementos(request,TipoDiagnostico, TipoDiagnosticoSerializer, idAux)


######### vistas para el Nomenclador Estado Solicitud ############
@csrf_exempt
def gestionarEstSolicitud(request, idAux = 0):
    return gestionarElementos(request,EstadoSolicitud, EstSolicitudSerializer, idAux)

######### vistas para el Nomenclador Tipo de Contrato ############
@csrf_exempt
def gestionarTipoContrato(request, idAux = 0):
    return gestionarElementos(request,TipoContrato, TipoContratoSerializer, idAux)

######### vistas para el Nomenclador Tipo de Curso ############
@csrf_exempt
def gestionarTipoCurso(request, idAux = 0):
    return gestionarElementos(request,TipoCurso, TipoCursoSerializer, idAux)

######### vistas para el Nomenclador Tipo de Solicitud ############
@csrf_exempt
def gestionarTipoSolicitud(request, idAux = 0):
    return gestionarElementos(request,TipoSolicitud, TipoSolicitudSerializer, idAux)

######### vistas para el Nomenclador Tipo de entidad ############
@csrf_exempt
def gestionarTipoEntidad(request, idAux = 0):
    return gestionarElementos(request,TipoEntidad, TipoEntidadSerializer, idAux)

######### vistas para el modelo Organismo ############
@csrf_exempt
def gestionarOrganismo(request, idAux = 0):
    return gestionarElementos(request,Organismo, OrganismoSerializer, idAux)

######### vistas para el Nomenclador Tipo de Servicio ############
@csrf_exempt
def gestionarTipoServicio(request, idAux = 0):
    return gestionarElementos(request,TipoServicio, TipoServicioSerializer, idAux)

######### vistas para el Nomenclador Tipo de Instrumento ############
@csrf_exempt
def gestionarTipoInstrumento(request, idAux = 0):
    return gestionarElementos(request,TipoInstrumento, TipoInstrumentoSerializer, idAux)

######### vistas para el Nomenclador Magnitud ############
@csrf_exempt
def gestionarMagnitud(request, idAux = 0):
    return gestionarElementos(request,Magnitud, MagnitudSerializer, idAux)

######### vistas para el Nomenclador Tipo de inspección ############
@csrf_exempt
def gestionarTipoInspeccion(request, idAux = 0):
    return gestionarElementos(request,TipoInspeccion, TipoInspeccionSerializer, idAux)

######### vistas para el Nomenclador Tipo de Especialista ############
@csrf_exempt
def gestionarTipoEspecialista(request, idAux = 0):
    return gestionarElementos(request,TipoEspecialista, TipoEspecialistaSerializer, idAux)

######### vistas para el Nomenclador Tipo de Norma ############
@csrf_exempt
def gestionarTipoNorma(request, idAux = 0):
    return gestionarElementos(request,TipoNorma, TipoNormaSerializer, idAux)

######### vistas para el Nomenclador Cargo ############
@csrf_exempt
def gestionarCargo(request, idAux = 0):
    return gestionarElementos(request,Cargo, CargoSerializer, idAux)

######### vistas para el Nomenclador Sector Económico ############
@csrf_exempt
def gestionarSectorEconomico(request, idAux = 0):
    return gestionarElementos(request,SectorEconomico, SectorEconomicoSerializer, idAux)

######### vistas para el Nomenclador Gestión de Certificado ############
@csrf_exempt
def gestionarGestCertificado(request, idAux = 0):
    return gestionarElementos(request,GestCertificado, GestCertificadoSerializer, idAux)

######### vistas para el Nomenclador Tematica ############
@csrf_exempt
def gestionarTematica(request, idAux = 0):
    return gestionarElementos(request,Tematica, TematicaSerializer, idAux)

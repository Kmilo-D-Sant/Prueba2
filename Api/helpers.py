from asyncio.windows_events import NULL
from inspect import Parameter
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def strToInt(cadena: str):
    try:
        if cadena == None or cadena == "":
            return 0
        i = int(cadena)
        return i
    except:
        return -1

def error(mensaje,errorCode=400):
    return JsonResponse({"error": mensaje, "datos": None},status=errorCode)

def errorMetodoNoPermitido(metodo):
    return error(f"Método no permitido ({metodo})")

def respuesta(datos,respCode=200):
    return JsonResponse({"error": None, "datos": datos},status=respCode)



@login_required
def gestionarElementos(request: Parameter, modelo: object, serializador: serializers, idAux: str):
    try:
        id = strToInt(idAux)
        if id < 0:
            return error("Parámetro no válido")

        if request.method == 'GET':
            if id == 0:
                objetos = modelo.objects.all()
                serializer = serializador(objetos, many=True)
                return respuesta(serializer.data)
            else:
                objeto = modelo.objects.get(id=id)
                serializer = serializador(objeto)
                return respuesta(serializer.data)

        if request.method == 'PUT':
            objeto = modelo.objects.get(id=id)        
            datos = JSONParser().parse(request)
            serializer = serializador(objeto,data=datos)
            if serializer.is_valid():
                objeto = serializer.save()
                if modelo == User:
                    objeto.set_password(objeto.password)
                    objeto.save()                   
                return respuesta(serializer.data)

        if request.method == 'POST':
            datos = JSONParser().parse(request)
            serializer = serializador(data=datos)
            if serializer.is_valid():
                objeto = serializer.save()
                if modelo == User:
                    objeto.set_password(objeto.password)
                    objeto.save()                   
                return respuesta(serializer.data)

        if request.method == 'DELETE':
            objeto = modelo.objects.get(id=id)
            serializer = serializador(objeto)
            objeto.delete()
            return respuesta(serializer.data)
            
        return error("Los datos no cumplen con los requisitos establecidos")
        
    except BaseException as err:
        print(str(type(err)))
        print(err)
        if str(type(err)).__contains__("DoesNotExist"):
            msg = "No existe el registro solicitado"
        else:
            msg = f"{err} ({type(err)})"
        return error(msg)




   
# @csrf_exempt
# def gestionarCliente(request, idAux = 0):
#     if request.method == 'GET':
#         id = strToInt(idAux)
#         if id < 0:
#             return JsonResponse(error("Parámetro no válido"))
#         elif(id == 0):
#             estudiantes = Estudiante.objects.all()
#             serializer = EstudianteSerializer(estudiantes, many = True)
#             return JsonResponse(respuesta(serializer.data), safe= False)
#         else:
#             token
#             return JsonResponse(respuesta(serializer.data), safe= False)
#     if request.method == 'PUT':
#         clienteDatos = JSONParser().parse(request)
#         cliente = Cliente.objects.get(id=clienteDatos['id'])
#         serializer = ClienteSerializer(cliente , data= clienteDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         cliente = JSONParser().parse(request)
#         serializer = ClienteSerializer(data =cliente)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estudiante no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         cliente = Cliente.objects.get(id= idAux)
#         cliente.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el modelo ControlCalidad ############
# @csrf_exempt
# def gestionarControlCalidad(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             controlCalidades = ControlCalidad.objects.all()
#             serializer = ControlCalidadSerializer(controlCalidades, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         controlCalidad = ControlCalidad.objects.filter(id = idAux)
#         serializer = ControlCalidadSerializer(instance= controlCalidad, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         controlCalidadDatos = JSONParser().parse(request)
#         controlCalidad = ControlCalidad.objects.get(id=controlCalidadDatos['id'])
#         serializer = ControlCalidadSerializer(controlCalidad , data= controlCalidadDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         controlCalidad = JSONParser().parse(request)
#         serializer = ControlCalidadSerializer(data =controlCalidad)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estudiante no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         controlCalidad = ControlCalidad.objects.get(id= idAux)
#         controlCalidad.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el modelo Curso ############
# @csrf_exempt
# def gestionarCurso(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             cursos = Curso.objects.all()
#             serializer = CursoSerializer(cursos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         curso = Curso.objects.filter(id = idAux)
#         serializer = CursoSerializer(instance= curso, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         cursoDatos = JSONParser().parse(request)
#         curso = Curso.objects.get(id=cursoDatos['id'])
#         serializer = CursoSerializer(curso , data= cursoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         curso = JSONParser().parse(request)
#         serializer = CursoSerializer(data =curso)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estudiante no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         curso = Curso.objects.get(id= idAux)
#         curso.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el modelo Entidad ############
# @csrf_exempt
# def gestionarEntidad(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             entidades = Entidad.objects.all()
#             serializer = EntidadSerializer(entidades, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         entidad = Entidad.objects.filter(id = idAux)
#         serializer = EntidadSerializer(instance= entidad, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         entidadDatos = JSONParser().parse(request)
#         entidad = Entidad.objects.get(id=entidadDatos['id'])
#         serializer = EntidadSerializer(entidad , data= entidadDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         entidad = JSONParser().parse(request)
#         serializer = EntidadSerializer(data =entidad)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estudiante no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         entidad = Entidad.objects.get(id= idAux)
#         entidad.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el modelo inspección || supervició ############
# @csrf_exempt
# def gestionarInspeccionSupervicion(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             inspeccionSuperviciones = InspeccionSupervicion.objects.all()
#             serializer = InspeccionSupervicionSerializer(inspeccionSuperviciones, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         inspeccionSupervicion = InspeccionSupervicion.objects.filter(id = idAux)
#         serializer = InspeccionSupervicionSerializer(instance= inspeccionSupervicion, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         inspeccionSupervicionDatos = JSONParser().parse(request)
#         inspeccionSupervicion = InspeccionSupervicion.objects.get(id=inspeccionSupervicionDatos['id'])
#         serializer = InspeccionSupervicionSerializer(inspeccionSupervicion , data= inspeccionSupervicionDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         inspeccionSupervicion = JSONParser().parse(request)
#         serializer = InspeccionSupervicionSerializer(data =inspeccionSupervicion)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estudiante no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         inspeccionSupervicion = InspeccionSupervicion.objects.get(id= idAux)
#         inspeccionSupervicion.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el modelo inspección || supervició ############
# @csrf_exempt
# def gestionarLevNorma(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             levNormas = LevNorma.objects.all()
#             serializer = LevNormaSerializer(levNormas, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         levNorma = LevNorma.objects.filter(id = idAux)
#         serializer = LevNormaSerializer(instance= levNorma, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         levNormaDatos = JSONParser().parse(request)
#         levNorma = LevNorma.objects.get(id=levNormaDatos['id'])
#         serializer = LevNormaSerializer(levNorma , data= levNormaDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         levNorma = JSONParser().parse(request)
#         serializer = LevNormaSerializer(data =levNorma)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estudiante no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         levNorma = LevNorma.objects.get(id= idAux)
#         levNorma.delete()
#         return JsonResponse("Eliminado con exito", safe=False)




# #################### NOMENCLADORES #############################


# ######### vistas para el Nomenclador Estado Contrato ############
# @csrf_exempt
# def gestionarEstContrato(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             estContratos = EstContrato.objects.all()
#             serializer = EstContratoSerializer(estContratos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         estContrato = EstContrato.objects.filter(id = idAux)
#         serializer = EstContratoSerializer(instance= estContrato, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         estContratoDatos = JSONParser().parse(request)
#         estContrato = EstContrato.objects.get(id=estContratoDatos['id'])
#         serializer = EstContratoSerializer(estContrato , data= estContratoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         estContrato = JSONParser().parse(request)
#         serializer = EstContratoSerializer(data =estContrato)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estado del contrato no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         estContrato = EstContrato.objects.get(id= idAux)
#         estContrato.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Estado Solicitud ############
# @csrf_exempt
# def gestionarEstSolicitud(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             estSolicitudes = EstSolicitud.objects.all()
#             serializer = EstSolicitudSerializer(estSolicitudes, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         estSolicitud = EstSolicitud.objects.filter(id = idAux)
#         serializer = EstSolicitudSerializer(instance= estSolicitud, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         estSolicitudDatos = JSONParser().parse(request)
#         estSolicitud = EstSolicitud.objects.get(id=estSolicitudDatos['id'])
#         serializer = EstSolicitudSerializer(estSolicitud , data= estSolicitudDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         estSolicitud = JSONParser().parse(request)
#         serializer = EstSolicitudSerializer(data =estSolicitud)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El estado de la solicitud no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         estSolicitud = EstSolicitud.objects.get(id= idAux)
#         estSolicitud.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de Contrato ############
# @csrf_exempt
# def gestionarTipoContrato(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoContratos = TipoContrato.objects.all()
#             serializer = TipoContratoSerializer(tipoContratos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoContrato = TipoContrato.objects.filter(id = idAux)
#         serializer = TipoContratoSerializer(instance= tipoContrato, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoContratoDatos = JSONParser().parse(request)
#         tipoContrato = TipoContrato.objects.get(id=tipoContratoDatos['id'])
#         serializer = TipoContratoSerializer(tipoContrato , data= tipoContratoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoContrato = JSONParser().parse(request)
#         serializer = TipoContratoSerializer(data =tipoContrato)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de contrato no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoContrato = TipoContrato.objects.get(id= idAux)
#         tipoContrato.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de Curso ############
# @csrf_exempt
# def gestionarTipoCurso(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoCursos = TipoCurso.objects.all()
#             serializer = TipoCursoSerializer(tipoCursos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoCurso = TipoCurso.objects.filter(id = idAux)
#         serializer = TipoCursoSerializer(instance= tipoCurso, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoCursoDatos = JSONParser().parse(request)
#         tipoCurso = TipoCurso.objects.get(id=tipoCursoDatos['id'])
#         serializer = TipoCursoSerializer(tipoCurso , data= tipoCursoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoCurso = JSONParser().parse(request)
#         serializer = TipoCursoSerializer(data =tipoCurso)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de curso no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoCurso = TipoCurso.objects.get(id= idAux)
#         tipoCurso.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de Solicitud ############
# @csrf_exempt
# def gestionarTipoSolicitud(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoSolicitudes = TipoSolicitud.objects.all()
#             serializer = TipoSolicitudSerializer(tipoSolicitudes, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoSolicitud = TipoSolicitud.objects.filter(id = idAux)
#         serializer = TipoSolicitudSerializer(instance= tipoSolicitud, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoSolicitudDatos = JSONParser().parse(request)
#         tipoSolicitud = TipoSolicitud.objects.get(id=tipoSolicitudDatos['id'])
#         serializer = TipoSolicitudSerializer(tipoSolicitud , data= tipoSolicitudDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoSolicitud = JSONParser().parse(request)
#         serializer = TipoSolicitudSerializer(data =tipoSolicitud)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de solicitud no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoSolicitud = TipoSolicitud.objects.get(id= idAux)
#         tipoSolicitud.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de entidad ############
# @csrf_exempt
# def gestionarTipoEntidad(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoEntidades = TipoEntidad.objects.all()
#             serializer = TipoEntidadSerializer(tipoEntidades, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoEntidad = TipoEntidad.objects.filter(id = idAux)
#         serializer = TipoEntidadSerializer(instance= tipoEntidad, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoEntidadDatos = JSONParser().parse(request)
#         tipoEntidad = TipoEntidad.objects.get(id=tipoEntidadDatos['id'])
#         serializer = TipoEntidadSerializer(tipoEntidad , data= tipoEntidadDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoEntidad = JSONParser().parse(request)
#         serializer = TipoEntidadSerializer(data =tipoEntidad)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de entidad no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoEntidad = TipoEntidad.objects.get(id= idAux)
#         tipoEntidad.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el modelo Organismo ############
# @csrf_exempt
# def gestionarOrganismo(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             organismos = Organismo.objects.all()
#             serializer = OrganismoSerializer(organismos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         organismo = Organismo.objects.filter(id = idAux)
#         serializer = OrganismoSerializer(instance= organismo, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         organismoDatos = JSONParser().parse(request)
#         organismo = Organismo.objects.get(id=organismoDatos['id'])
#         serializer = OrganismoSerializer(organismo , data= organismoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         organismo = JSONParser().parse(request)
#         serializer = OrganismoSerializer(data =organismo)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El organismo no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         organismo = Organismo.objects.get(id= idAux)
#         organismo.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de Servicio ############
# @csrf_exempt
# def gestionarTipoServicio(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoServicios = TipoServicio.objects.all()
#             serializer = TipoServicioSerializer(tipoServicios, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoServicio = TipoServicio.objects.filter(id = idAux)
#         serializer = TipoServicioSerializer(instance= tipoServicio, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoServicioDatos = JSONParser().parse(request)
#         tipoServicio = TipoServicio.objects.get(id=tipoServicioDatos['id'])
#         serializer = TipoServicioSerializer(tipoServicio , data= tipoServicioDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoServicio = JSONParser().parse(request)
#         serializer = TipoServicioSerializer(data =tipoServicio)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de servicio no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoServicio = TipoServicio.objects.get(id= idAux)
#         tipoServicio.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de Instrumento ############
# @csrf_exempt
# def gestionarTipoInstrumento(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoInstrumentos = TipoInstrumento.objects.all()
#             serializer = TipoServicioSerializer(tipoInstrumentos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoInstrumento = TipoInstrumento.objects.filter(id = idAux)
#         serializer = TipoServicioSerializer(instance= tipoInstrumento, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoInstrumentoDatos = JSONParser().parse(request)
#         tipoInstrumento = TipoInstrumento.objects.get(id=tipoInstrumentoDatos['id'])
#         serializer = TipoServicioSerializer(tipoInstrumento , data= tipoInstrumentoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoInstrumento = JSONParser().parse(request)
#         serializer = TipoServicioSerializer(data =tipoInstrumento)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de instrumento no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoInstrumento = TipoInstrumento.objects.get(id= idAux)
#         tipoInstrumento.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Magnitud ############
# @csrf_exempt
# def gestionarMagnitud(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             magnitudes = Magnitud.objects.all()
#             serializer = MagnitudSerializer(magnitudes, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         magnitud = Magnitud.objects.filter(id = idAux)
#         serializer = MagnitudSerializer(instance= magnitud, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         magnitudDatos = JSONParser().parse(request)
#         magnitud = Magnitud.objects.get(id=magnitudDatos['id'])
#         serializer = MagnitudSerializer(magnitud , data= magnitudDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         magnitud = JSONParser().parse(request)
#         serializer = MagnitudSerializer(data =magnitud)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("La magnitud no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         magnitud = Magnitud.objects.get(id= idAux)
#         magnitud.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de inspección ############
# @csrf_exempt
# def gestionarTipoInspeccion(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoInspecciones = TipoInspeccion.objects.all()
#             serializer = TipoInspeccionSerializer(tipoInspecciones, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoInspeccion = TipoInspeccion.objects.filter(id = idAux)
#         serializer = TipoInspeccionSerializer(instance= tipoInspeccion, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoInspeccionDatos = JSONParser().parse(request)
#         tipoInspeccion = TipoInspeccion.objects.get(id=tipoInspeccionDatos['id'])
#         serializer = TipoInspeccionSerializer(tipoInspeccion , data= tipoInspeccionDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoInspeccion = JSONParser().parse(request)
#         serializer = TipoInspeccionSerializer(data =tipoInspeccion)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de inspección no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoInspeccion = TipoInspeccion.objects.get(id= idAux)
#         tipoInspeccion.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de Especialista ############
# @csrf_exempt
# def gestionarTipoEspecialista(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoEspecialistas = TipoEspecialista.objects.all()
#             serializer = TipoEspecialistaSerializer(tipoEspecialistas, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoEspecialista = TipoEspecialista.objects.filter(id = idAux)
#         serializer = TipoEspecialistaSerializer(instance= tipoEspecialista, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoEspecialistaDatos = JSONParser().parse(request)
#         tipoEspecialista = TipoEspecialista.objects.get(id=tipoEspecialistaDatos['id'])
#         serializer = TipoEspecialistaSerializer(tipoEspecialista , data= tipoEspecialistaDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoEspecialista = JSONParser().parse(request)
#         serializer = TipoEspecialistaSerializer(data =tipoEspecialista)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de especialista no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoEspecialista = TipoEspecialista.objects.get(id= idAux)
#         tipoEspecialista.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tipo de Norma ############
# @csrf_exempt
# def gestionarTipoNorma(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tipoNormas = TipoNorma.objects.all()
#             serializer = TipoNormaSerializer(tipoNormas, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tipoNorma = TipoNorma.objects.filter(id = idAux)
#         serializer = TipoNormaSerializer(instance= tipoNorma, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tipoNormaDatos = JSONParser().parse(request)
#         tipoNorma = TipoNorma.objects.get(id=tipoNormaDatos['id'])
#         serializer = TipoNormaSerializer(tipoNorma , data= tipoNormaDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tipoNorma = JSONParser().parse(request)
#         serializer = TipoNormaSerializer(data =tipoNorma)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El tipo de norma no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tipoNorma = TipoNorma.objects.get(id= idAux)
#         tipoNorma.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Cargo ############
# @csrf_exempt
# def gestionarCargo(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             cargos = Cargo.objects.all()
#             serializer = CargoSerializer(cargos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         cargo = Cargo.objects.filter(id = idAux)
#         serializer = CargoSerializer(instance= cargo, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         cargoDatos = JSONParser().parse(request)
#         cargo = Cargo.objects.get(id=cargoDatos['id'])
#         serializer = CargoSerializer(cargo , data= cargoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         cargo = JSONParser().parse(request)
#         serializer = CargoSerializer(data =cargo)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El cargo no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         cargo = Cargo.objects.get(id= idAux)
#         cargo.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Sector Económico ############
# @csrf_exempt
# def gestionarSectorEconomico(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             sectorEconomicos = SectorEconomico.objects.all()
#             serializer = SectorEconomicoSerializer(sectorEconomicos, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         sectorEconomico = SectorEconomico.objects.filter(id = idAux)
#         serializer = SectorEconomicoSerializer(instance= sectorEconomico, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         sectorEconomicoDatos = JSONParser().parse(request)
#         sectorEconomico = SectorEconomico.objects.get(id=sectorEconomicoDatos['id'])
#         serializer = SectorEconomicoSerializer(sectorEconomico , data= sectorEconomicoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         sectorEconomico = JSONParser().parse(request)
#         serializer = SectorEconomicoSerializer(data =sectorEconomico)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("El sector económico no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         sectorEconomico = SectorEconomico.objects.get(id= idAux)
#         sectorEconomico.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Gestión de Certificado ############
# @csrf_exempt
# def gestionarGestCertificado(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             gestCertificados = GestCertificado.objects.all()
#             serializer = GestCertificadoSerializer(gestCertificados, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         gestCertificado = GestCertificado.objects.filter(id = idAux)
#         serializer = GestCertificadoSerializer(instance= gestCertificado, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         gestCertificadoDatos = JSONParser().parse(request)
#         gestCertificado = GestCertificado.objects.get(id=gestCertificadoDatos['id'])
#         serializer = GestCertificadoSerializer(gestCertificado , data= gestCertificadoDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         gestCertificado = JSONParser().parse(request)
#         serializer = GestCertificadoSerializer(data =gestCertificado)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("La gestión de certificado no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         gestCertificado = GestCertificado.objects.get(id= idAux)
#         gestCertificado.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

# ######### vistas para el Nomenclador Tematica ############
# @csrf_exempt
# def gestionarTematica(request, idAux = 0):
#     if request.method == 'GET':
#         if(idAux == 0):
#             tematicas = Tematica.objects.all()
#             serializer = TematicaSerializer(tematicas, many = True)
#             return JsonResponse(serializer.data, safe= False)
#         tematica = Tematica.objects.filter(id = idAux)
#         serializer = TematicaSerializer(instance= tematica, many = True)
#         return JsonResponse(serializer.data, safe= False)
#     if request.method == 'PUT':
#         tematicaDatos = JSONParser().parse(request)
#         tematica = Tematica.objects.get(id=tematicaDatos['id'])
#         serializer = TematicaSerializer(tematica , data= tematicaDatos)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Actualización exitosa", safe=False)
#         return JsonResponse("Los datos no cumplen el estandar establecido", safe=False)
#     if request.method =='POST':
#         tematica = JSONParser().parse(request)
#         serializer = TematicaSerializer(data =tematica)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("Añadido con exito", safe=False)
#         return JsonResponse("La temática no cumple con los requisitos establecidos ", safe=False)
#     if request.method== 'DELETE':
#         tematica = Tematica.objects.get(id= idAux)
#         tematica.delete()
#         return JsonResponse("Eliminado con exito", safe=False)

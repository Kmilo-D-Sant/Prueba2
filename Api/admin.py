
from csv import list_dialects
from pyexpat import model
from re import search
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from.models import NotasCurso,NormaCuba,Diagnostico, LevNorma, InspeccionSupervicion,ControlCalidad ,Cliente, Entidad, EstadoSolicitud, Magnitud, Organismo,TipoDiagnostico, TipoEntidad,Tematica, TipoEspecialista, TipoInspeccion,TipoCurso,EstadoContrato, TipoContrato, TipoSolicitud, TipoServicio, TipoInstrumento, TipoNorma, Estudiante, Curso,GestCertificado, Cargo, SectorEconomico, Isos, NormaResolucion


# Register your models here.
# admin.site.register(Usuario, UserAdmin)
admin.site.register(TipoContrato)
admin.site.register(TipoDiagnostico)
admin.site.register(TipoCurso)
admin.site.register(EstadoContrato)
admin.site.register(EstadoSolicitud)
admin.site.register(TipoSolicitud)
admin.site.register(TipoEntidad)
admin.site.register(Organismo)
admin.site.register(TipoServicio)
admin.site.register(TipoInstrumento)
admin.site.register(Magnitud)
admin.site.register(TipoInspeccion)
admin.site.register(Tematica)
admin.site.register(TipoEspecialista)
admin.site.register(TipoNorma)
admin.site.register(Cargo)
admin.site.register(SectorEconomico)
admin.site.register(GestCertificado)
admin.site.register(Isos)
admin.site.register(NormaResolucion)


admin.site.register(Diagnostico)
# admin.site.register(AdjuntarArchivo)



 



@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido1','apellido2')
    list_display_links = ('nombre','apellido1','apellido2')
    search_fields = ('nombre','apellido1','apellido2')
    list_filter = ('nombre',)
    list_per_page = 20
    #exclude = ('') => permite ver el valor pero no editarlo ni adicionarlo

class NotasCursoInLine(admin.TabularInline):
    model = NotasCurso
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [NotasCursoInLine,]
    list_display = ('nombre','Tipo','profesor','fechaInicio','duracionDias')
    list_display_links = ('nombre','Tipo','profesor','fechaInicio','duracionDias')
    search_fields = ('Tipo','nombre','profesor','Tematica')
    list_filter = ('Tipo','Tematica')
    list_per_page = 20

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido1','empresa','email','telefono','abonado')
    list_display_links = ('nombre','apellido1','empresa','email','telefono','abonado')
    search_fields = ('nombre','apellido1','apellido2','ci','telefono','email')
    list_filter = ('Organismo','empresa','Cargo','abonado')
    list_per_page = 20   


@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ('nombre','organismo','establecimientoDireccion')
    list_display_links = ('nombre','organismo','establecimientoDireccion')
    search_fields = ('nombre','organismo','establecimientoDireccion','establecimiento','directorEntidad')
    list_filter = ('organismo','abonado')
    list_per_page = 20


@admin.register(LevNorma)
class LevNormaAdmin(admin.ModelAdmin):
    list_display = ('nombreNorma','numNorma','tipo','annoNorma')
    list_display_links = ('nombreNorma','numNorma','tipo','annoNorma')
    search_fields = ('nombreNorma','numNorma','tipo','annoNorma','productoServicio')
    list_filter = ('tipo','annoNorma')
    list_per_page = 20

@admin.register(InspeccionSupervicion)
class InspeccionSupervicionAdmin(admin.ModelAdmin):
    list_display = ('entidad','tipo','codigo','fechaInspeccion')
    list_display_links = ('entidad','tipo','codigo','fechaInspeccion')
    search_fields = ('entidad','tipo','codigo','objetoInspeccion')
    list_filter = ('entidad','tipo')
    list_per_page = 20

@admin.register(ControlCalidad)
class ControlCalidadAdmin(admin.ModelAdmin):
    list_display = ('entidad','capitulo','articulo','cumplio')
    list_display_links = ('entidad','capitulo','articulo','cumplio')
    search_fields = ('entidad','capitulo')
    list_filter = ('cumplio','articulo')
    list_per_page = 20

@admin.register(NormaCuba)
class NormaCubaAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero')
    list_display_links = ('nombre','numero')
    search_fields = ('nombre','numero',)
    list_filter = ('resolucion','iso','tipoNorma')
    list_per_page = 20


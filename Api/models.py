from dataclasses import field
from importlib.resources import contents
from pyexpat import model
from queue import Empty
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django import forms
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import AbstractBaseUser
#from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



####### Modelado de Usuario #######

# class GestionUsuario(BaseUserManager):
#     def create_user(self, correo,username, nombre,apellidos, password = None ):
#         if not correo:
#             raise ValueError('El usuario debe tener correo')
        
#         correo = self.normalize_email(correo)
#         usuario = self.model( correo = correo,username = username, nombre = nombre, apellidos=apellidos)
        
#         usuario.set_password(password)
#         #usuario.save(using = self._db)
#         usuario.save()
        
#         return usuario
    
#     def create_superuser(self, correo,username, nombre,apellidos, password ):
#         usuario = self.create_user(correo = correo,username = username, nombre = nombre, apellidos=apellidos)
#         usuario.administador = True
#         usuario.save()

#         return usuario

######### Usuario #############
# class Usuario(AbstractBaseUser):
#     username = models.CharField('Nombre de usuario', unique= True, max_length=100)
#     correo = models.EmailField('Correo', max_length=100, unique=True)
#     nombre = models.CharField('Nombre', max_length=100, blank=True, null=True)
#     apellidos = models.CharField('Apellidos', max_length=100, blank=True, null=True)
#     activo = models.BooleanField(default=False)
#     administador = models.BooleanField(default=False)
#     object = GestionUsuario()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['correo','nombre','apellidos']
    
#     def __str__(self):
#         return f'{self.nombre}, {self.apellidos}'

#     def has_perm(self, perm, ob):
#         return True

#     def has_module_perms(self, app_label):
#         return  True
#     @property
#     def is_staff(self):
#         return self.administador    



####### Nomencladores ##########
class TipoContrato(models.Model):
    
    tipo = models.CharField( max_length= 50)

    class Meta:
        verbose_name = "Tipo de contrato"
        verbose_name_plural = "Tipos de contratos"
    
    def __str__(self):
        texto = self.tipo
        return  texto
    
class TipoCurso(models.Model):
    tipo = models.CharField("Tipo",max_length= 50)

    class Meta:
        verbose_name = "Tipo de curso"
        verbose_name_plural = "Tipos de cursos"

    def __str__(self):
        texto = self.tipo
        return  texto

class EstadoContrato(models.Model):
    estado = models.CharField("Estado", max_length= 50, null = True)
    
    class Meta:
        verbose_name = "Estado del contrato"
        verbose_name_plural = "Estados de contratos"

    def __str__(self):
        texto = self.estado
        return  texto

class EstadoSolicitud(models.Model):
    
    estado = models.CharField("Estado", max_length= 50)

    class Meta:
        verbose_name = "Estado de solicitud"
        verbose_name_plural = "Estados de solicitudes"

    def __str__(self):
        texto = self.estado
        return  texto

class TipoSolicitud(models.Model):
    
    tipo = models.CharField( "Tipo", max_length= 50)
    
    class Meta:
        verbose_name = "Tipo de solicitud"
        verbose_name_plural = "Tipos de solicitudes"
    
    def __str__(self):
        texto = self.tipo
        return  texto
    
class TipoEntidad(models.Model):
    
    tipo = models.CharField("Tipo", max_length= 50)

    class Meta:
        verbose_name = "Tipo de entidad"
        verbose_name_plural = "Tipos de entidades"

    def __str__(self):
        texto = self.tipo
        return  texto

class Organismo(models.Model):
    nombre = models.CharField("Nombre", max_length= 50)

    def __str__(self):
        texto = self.nombre
        return  texto                

class TipoServicio(models.Model):
    
    tipo = models.CharField("Tipo", max_length= 50)

    class Meta:
        verbose_name = "Tipo de servicio"
        verbose_name_plural = "Tipos de servicios"

    def __str__(self):
        texto = self.tipo
        return  texto  

# class Tipo_Documento(models.Model):
    
#     tipo = models.CharField( "Tipo", max_length= 50)

#     class Meta:
#         verbose_name = "Tipo de documento"
#         verbose_name_plural = "Tipos de documentos"

#     def __str__(self):
#         texto = self.tipo
#         return  texto

class TipoInstrumento(models.Model):
    
    tipo = models.CharField( "Tipo", max_length= 50)

    class Meta:
        verbose_name = "Tipo de instrumento"
        verbose_name_plural = "Tipos de instrumentos"

    def __str__(self):
        texto = self.tipo
        return  texto

class Magnitud(models.Model):
    
    magnitud = models.CharField( "Magnitud", max_length= 50)

    class Meta:
        verbose_name_plural = "Magnitudes"

    def __str__(self):
        texto = self.magnitud
        return  texto

class TipoInspeccion(models.Model):
    
    tipo = models.CharField( "Tipo", max_length= 50)

    class Meta:
        verbose_name = "Tipo de inspección"
        verbose_name_plural = "Tipos de inspecciones"

    def __str__(self):
        texto = self.tipo
        return  texto

class Tematica(models.Model):
    
    nombre = models.CharField( "Nombre", max_length= 50)

    class Meta:
        verbose_name = "Temática"
        verbose_name_plural = "Temáticas"

    def __str__(self):
        texto = self.nombre
        return  texto

class TipoEspecialista(models.Model):
    
    tipo = models.CharField( "Tipo", max_length= 50)

    class Meta:
        verbose_name = "Tipo de especialista"
        verbose_name_plural = "Tipos de especialistas"

    def __str__(self):
        texto = self.tipo
        return  texto

class TipoNorma(models.Model):
    Tipo = models.CharField("Tipo", max_length= 50)
    codigo = models.SmallIntegerField("Código")

    class Meta:
        verbose_name = "Tipo de norma"
        verbose_name_plural = "Tipos de normas"

    def __str__(self):
        texto = self.Tipo
        return  texto

class Cargo(models.Model):
    nombre = models.CharField("Nombre", max_length= 50)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        texto = self.nombre
        return  texto

class SectorEconomico(models.Model):
    nombre = models.CharField("Nombre", max_length= 50)

    class Meta:
        verbose_name = "Sector económico"
        verbose_name_plural = "Sectores económicos"

    def __str__(self):
        texto = self.nombre
        return  texto

class GestCertificado(models.Model):
    nombre = models.CharField("Nombre", max_length= 50)

    class Meta:
        verbose_name = "Gestión de certificado"
        verbose_name_plural = "Gestión de certificados"

    def __str__(self):
        texto = self.nombre
        return  texto

class TipoDiagnostico(models.Model):
    tipo = models.CharField("Tipo", max_length= 50)

    class Meta:
        verbose_name = "Tipo de diagnóstico"
        verbose_name_plural = "Tipo de diagnósticos"

    def __str__(self):
        texto = self.tipo
        return  texto




######## modelos #######

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField("Primer apellido",max_length=20)
    apellido2 = models.CharField("Segundo apellido",max_length=20)
    

    class Meta:
        verbose_name="Estudiante"

    def __srt__(self):
        texto = self.nombre
        return  texto

class Cliente(models.Model):
    nombre = models.CharField(max_length= 40)
    apellido1 = models.CharField("Primer Apellido",max_length=20)
    apellido2 = models.CharField("Segundo Apellido",max_length=20)
    ci = models.FloatField("Número de carnet")
    Cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null = True)
    empresa = models.CharField(max_length=50)
    Sector_Economico = models.ForeignKey(SectorEconomico,on_delete=models.CASCADE, null= True)
    nacionalidad = models.CharField("Nacionalidad",max_length=50)
    direccion = models.CharField("Dirección",max_length=80) 
    Organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE, null= True)
    abonado = models.BooleanField(default=False)#si/no
    telefono = models.FloatField()
    email = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    nit = models.BigIntegerField('NIT')

    def __str__(self):
        return self.nombre  +" "+  self.apellido1 +" " +  self.apellido2 + " ("+ self.empresa + ")"

class Curso(models.Model):
    Tipo = models.ForeignKey(TipoCurso, on_delete=models.CASCADE,null = True)
    fechaInicio = models.DateField('Fecha de inicio')
    fechaFin = models.DateField('Fecha de fin')
    nombre = models.CharField(max_length=30,blank=False)
    profesor = models.CharField(max_length= 20,blank=False)
    duracionDias = models.SmallIntegerField("Días de duración",blank=False)
    horasTotales = models.SmallIntegerField("Horas de duración")
    descripción = models.CharField(max_length= 500)
    enlaceMoodle =  models.URLField(max_length=300)
    Cliente = models.ManyToManyField(Cliente, through = 'NotasCurso')
    Tematica = models.ManyToManyField(Tematica)
    costo = models.SmallIntegerField("Costo")

    def __str__(self):
        texto = self.nombre
        return  texto 

class NotasCurso(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.SmallIntegerField('Nota')

    def __str__(self):
        return  str(self.id) + '-' + self.Cliente.nombre

class informacionComun(models.Model):
    nombre = models.CharField(max_length= 40)
    direccion = models.CharField("Dirección",max_length=80) 
    Organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE, null= True)
    abonado = models.BooleanField(default=False)#si/no
    telefono = models.FloatField()
    email = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    nit = models.BigIntegerField('NIT')

    class Meta:
        abstract = True

class Entidad (models.Model):
    nombre = models.CharField(max_length= 40)
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE, null= True)
    abonado = models.BooleanField(default=False)#si/no
    telefono = models.FloatField()
    email = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    nit = models.BigIntegerField('NIT')
    establecimientoDireccion = models.CharField("Dirección",max_length=80) 
    establecimiento = models.CharField(max_length= 50)
    #sisGestCertificado = models.CharField("Sistema de gestión certificado",max_length= 100)
    gestionCertificado = models.ForeignKey(GestCertificado, on_delete= models.CASCADE)
    nombreEspecialista = models.CharField("Especialista de calidad",max_length=80)
    directorEntidad = models.CharField("Director de la entidad", max_length= 80)
    directorEstablecimiento = models.CharField("Director del establecimiento", max_length=80)

    class Meta:
        verbose_name_plural = "Entidades"

    def __str__(self):
        texto = self.nombre
        return  texto 

class Contrato(models.Model):
    numero = models.SmallIntegerField('Número del contrato')
    anno = models.SmallIntegerField('Año')
    otraPate = models.CharField('Otra parte',max_length=100)
    codigoReeup = models.SmallIntegerField('Código REEUP')
    cuentaBancaria = models.BigIntegerField('Cuenta bancaria en CUP')
    representante = models.CharField("Representante", max_length=50)
    caracter = models.CharField('Caracter', max_length=20)
    resolucion  = models.SmallIntegerField()
    fechaResolucion = models.DateField()
    emitidaPor = models.CharField('Emitida por', max_length=100)
    cargo = models.CharField('Cargo', max_length=50)

    class Meta:
        verbose_name_plural = "Contratos"

    def __str__(self):
        texto = self.nombre
        return  texto

#Reporte de levantamiento de norma
class LevNorma(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    productoServicio = models.BooleanField()
    nombreNorma = models.CharField("Nombre de la norma", max_length=40)
    numNorma = models.FloatField()
    tipo = models.ForeignKey(TipoNorma, on_delete= models.CASCADE, null= False)
    annoNorma = models.BigIntegerField("Año")

    class Meta:
        verbose_name = "Levantamiento de norma"
        verbose_name_plural = "Levantamientos de normas"

    def __str__(self):
        texto = self.nombreNorma
        return  texto 


#***************  clase con dudas  ***************


#Registro de norma de empresa

# class RegNormaEmp(models.Model):
#     cliente = models.OneToOneField(Cliente, on_delete= models.CASCADE, null=False)
#     campos de la BD de la empresa
#     def __str__(self):
#         return "Registro de normas"


class InspeccionSupervicion(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete= models.CASCADE)
    tipo = models.ForeignKey(TipoEntidad, on_delete=models.CASCADE, null= False)
    codigo = models.CharField(max_length=20)
    objetoInspeccion = models.CharField("Objeto de inspección", max_length=80 )
    destinoProduccion = models.CharField("Destino de la producción", max_length= 80)
    fechaInspeccion = models.DateField("Fecha de la inspección")
    fechaEmisionInf = models.DateField("Fecha de emisión del informe")
    noConfDetectadas = models.CharField("No conformidades detectadas", max_length=2000)
    #documentoViolado = models.OneToOneField(Tipo_Documento, on_delete=models.CASCADE)
    Conforme = models.CharField(max_length=2000)
    nombreInspector = models.CharField("Inspector", max_length=50)

    class Meta:
        verbose_name = "Inspección / supervisión"
        verbose_name_plural = "Inspecciones y superviciones"

    def __str__(self):
        return "Inspección a "+ self.objetoInspeccion +" dia "+ self.fechaInspeccion
    #•	Medidas aplicadas:
	        # Obligación de hacer 
            #     Suspensión
            #     Erradicar no conformidades
	        #     Fecha de cumplimiento
	        # Multa
            #     Por incumplimiento
            #         Normalización
            #         Metrología 
	        #     Monto 

class ControlCalidad(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    capitulo = models.CharField("Capítulo",max_length=20)
    articulo = models.CharField("Artículo",max_length=20)
    hallazgo = models.CharField(max_length=2000)
    cumplio = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Control de calidad"
        verbose_name_plural = "Controles de calidad"

    def __str__(self):
        return "Control de calidad a la entidad "+ self.entidad.nombre


# class AdjuntarArchivo(forms.Form):
#     nombreArchivo = models.CharField(max_length= 50)
#     archivo = forms.FileField()
#     Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     TipoDiagnostico = models.ForeignKey(TipoDiagnostico, on_delete=models.CASCADE)
    

def documentoDiagnostico(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'media/diagnostico_{0}/{1}'.format(instance.id, filename)


class Diagnostico(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    TipoDiagnostico = models.ForeignKey(TipoDiagnostico, on_delete=models.CASCADE)
    archivoAdjunto = models.FileField(upload_to=documentoDiagnostico, null=True)
    # AdjuntarArchivo = File(file_field = content_file)
    class Meta:
        verbose_name = "Diagnóstico"
        verbose_name_plural = "Diagnóstico"

    def __str__(self):
        return  'Diagnóstico' 

    



#********** modelo Normas ********

class NormaResolucion(models.Model):
    numero = models.CharField("Número",max_length= 30)
    descripcion = models.CharField("Descripción", max_length=30)
    
    class Meta:
        verbose_name = "Resolución de la norma"
        verbose_name_plural = "Resoluciones de normas"

    def __str__(self):
        return "Norma número "+ self.numero

class Isos(models.Model):
    numero = models.CharField("Número", max_length=20)
    descripcion = models.CharField("Descripción", max_length= 500)
    class Meta:
        verbose_name_plural = "Isos"
    
    def __str__(self):
        return "Iso número "+ self.numero

class NormaCuba(models.Model):
    fechaExcepcion = models.DateField()
    nombre = models.CharField( max_length= 20)
    numero = models.CharField(max_length= 20)
    anno = models.SmallIntegerField("año")
    pagina = models.SmallIntegerField("Página")
    resolucion = models.ForeignKey(NormaResolucion, on_delete=models.CASCADE)
    fechaValidacion = models.DateField("Fecha de validación")
    fechaRegistro = models.DateField("Fecha de registro")
    fechaAprovacion = models.DateField("Fecha de aprovación")
    formatoDisponible = models.SmallIntegerField("Formato")
    tipoNorma = models.ForeignKey(TipoNorma, on_delete=models.CASCADE)
    precio = models.SmallIntegerField()
    observacion = models.CharField("Observación", max_length=80)
    iso = models.ManyToManyField(Isos)

    class Meta:
        verbose_name = "Norma"
        verbose_name_plural = "Normas de Cuba"

    def __str__(self):
        return self.nombre +"("+self.numero+")"

########## asociar las notas de los usuarios con el curso
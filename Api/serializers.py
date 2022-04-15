from rest_framework import serializers
from . models import Estudiante,Diagnostico,TipoDiagnostico ,Cliente, Entidad, Curso, ControlCalidad, InspeccionSupervicion, LevNorma, EstadoContrato, EstadoSolicitud,Tematica, TipoContrato, TipoCurso, TipoSolicitud,  TipoEntidad, Organismo, TipoServicio, TipoInstrumento, Magnitud, TipoInspeccion, TipoEspecialista, TipoNorma, Cargo, SectorEconomico, GestCertificado, NormaResolucion, Isos, NormaCuba  
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry


########### Log ##########
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'

########### Usuario ##########
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

########### Nomencladores ########
class EstContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoContrato
        fields = '__all__'

class EstSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSolicitud
        fields = '__all__'

class TipoContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContrato
        fields = '__all__'

class TipoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCurso
        fields = '__all__'

class TipoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSolicitud
        fields = '__all__'

class TipoEntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEntidad
        fields = '__all__'

class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        fields = '__all__'      

class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = '__all__'     

class TipoInstrumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInstrumento
        fields = '__all__' 

class MagnitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magnitud
        fields = '__all__' 

class TipoInspeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInspeccion
        fields = '__all__' 

class TipoEspecialistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEspecialista
        fields = '__all__'

class TipoNormaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoNorma
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class SectorEconomicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectorEconomico
        fields = '__all__'

class GestCertificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GestCertificado
        fields = '__all__'

class TematicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tematica
        fields = '__all__'

class TipoDiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDiagnostico
        fields = '__all__'

########### modelos #############

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = '__all__'

class ControlCalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlCalidad
        fields = '__all__'

class InspeccionSupervicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspeccionSupervicion
        fields = '__all__'

class LevNormaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevNorma
        fields = '__all__'


########### Normas ###########

class NormaResolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormaResolucion
        fields = '__all__ '

class IsosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isos
        fields = '__all__ '

class NormaCubaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormaCuba
        fields = '__all__ '
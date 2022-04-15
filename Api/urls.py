from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('trazas', views.trazas),
    path('trazas/', views.trazas),

    path('acceder/', views.iniciarSesion),
    path('salir/', views.cerrarSesion),
    
    path('gestionar-usuarios', views.gestionarUsuario),
    path('gestionar-usuarios/', views.gestionarUsuario),
    path('gestionar-usuarios/<str:idAux>', views.gestionarUsuario),

    path('gestionar-estudiantes', views.gestionarEstudiante),
    path('gestionar-estudiantes/', views.gestionarEstudiante),
    path('gestionar-estudiantes/<str:idAux>', views.gestionarEstudiante),

    path('gestionar-clientes', views.gestionarCliente),
    path('gestionar-clientes/', views.gestionarCliente),
    path('gestionar-clientes/<str:idAux>', views.gestionarCliente),

    path('gestionar-control-calidad', views.gestionarEstudiante),
    path('gestionar-control-calidad/', views.gestionarEstudiante),
    path('gestionar-control-calidad/<str:idAux>', views.gestionarEstudiante),
    
    path('gestionar-cursos', views.gestionarCurso),
    path('gestionar-cursos/', views.gestionarCurso),
    path('gestionar-cursos/<str:idAux>', views.gestionarCurso),


    path('gestionar-entidades', views.gestionarEntidad),
    path('gestionar-entidades/', views.gestionarEntidad),
    path('gestionar-entidades/<str:idAux>', views.gestionarEntidad),

    path('gestionar-inspecciones', views.gestionarEntidad),
    path('gestionar-inspecciones/', views.gestionarEntidad),
    path('gestionar-inspecciones/<str:idAux>', views.gestionarEntidad),

    path('gestionar-normas', views.gestionarEntidad),
    path('gestionar-normas/', views.gestionarEntidad),
    path('gestionar-normas/<str:idAux>', views.gestionarEntidad),
 

    ###################### Urls nomencladores ###########################

    path('gestionar-estado-contratos', views.gestionarEstContrato),
    path('gestionar-estado-contratos/', views.gestionarEstContrato),
    path('gestionar-estado-contratos/<str:idAux>', views.gestionarEstContrato),
    
    path('gestionar-estado-solicitudes', views.gestionarEstSolicitud),
    path('gestionar-estado-solicitudes/', views.gestionarEstSolicitud),
    path('gestionar-estado-solicitudes/<str:idAux>', views.gestionarEstSolicitud),
    
    path('gestionar-tipo-contratos', views.gestionarTipoContrato),
    path('gestionar-tipo-contratos/', views.gestionarTipoContrato),
    path('gestionar-tipo-contratos/<str:idAux>', views.gestionarTipoContrato),
    
    path('gestionar-tipo-cursos', views.gestionarTipoCurso),
    path('gestionar-tipo-cursos/', views.gestionarTipoCurso),
    path('gestionar-tipo-cursos/<str:idAux>', views.gestionarTipoCurso),
    
    path('gestionar-tipo-solicitudes', views.gestionarTipoSolicitud),
    path('gestionar-tipo-solicitudes/', views.gestionarTipoSolicitud),
    path('gestionar-tipo-solicitudes/<str:idAux>', views.gestionarTipoSolicitud),
    
    path('gestionar-tipo-entidades', views.gestionarTipoEntidad),
    path('gestionar-tipo-entidades/', views.gestionarTipoEntidad),
    path('gestionar-tipo-entidades/<str:idAux>', views.gestionarTipoEntidad),
    
    path('gestionar-organismos', views.gestionarOrganismo),
    path('gestionar-organismos/', views.gestionarOrganismo),
    path('gestionar-organismos/<str:idAux>', views.gestionarOrganismo),

    path('gestionar-tipo-servicios', views.gestionarTipoServicio),
    path('gestionar-tipo-servicios/', views.gestionarTipoServicio),
    path('gestionar-tipo-servicios/<str:idAux>', views.gestionarTipoServicio),

    path('gestionar-tipo-instrumentos', views.gestionarTipoInstrumento),
    path('gestionar-tipo-instrumentos/', views.gestionarTipoInstrumento),
    path('gestionar-tipo-instrumentos/<str:idAux>', views.gestionarTipoInstrumento),

    path('gestionar-magnitudes', views.gestionarMagnitud),
    path('gestionar-magnitudes/', views.gestionarMagnitud),
    path('gestionar-magnitudes/<str:idAux>', views.gestionarMagnitud),
    
    path('gestionar-tipo-inspecciones', views.gestionarTipoInspeccion), 
    path('gestionar-tipo-inspecciones/', views.gestionarTipoInspeccion),
    path('gestionar-tipo-inspecciones/<str:idAux>', views.gestionarTipoInspeccion),

    path('gestionar-tipo-especialistas', views.gestionarTipoEspecialista), 
    path('gestionar-tipo-especialistas/', views.gestionarTipoEspecialista),
    path('gestionar-tipo-especialistas/<str:idAux>', views.gestionarTipoEspecialista),

    path('gestionar-tipo-normas', views.gestionarTipoNorma),
    path('gestionar-tipo-normas/', views.gestionarTipoNorma),
    path('gestionar-tipo-normas/<str:idAux>', views.gestionarTipoNorma),

    path('gestionar-cargos', views.gestionarCargo),
    path('gestionar-cargos/', views.gestionarCargo),
    path('gestionar-cargos/<str:idAux>', views.gestionarCargo),

    path('gestionar-sector-economicos', views.gestionarSectorEconomico),
    path('gestionar-sector-economicos/', views.gestionarSectorEconomico),
    path('gestionar-sector-economicos/<str:idAux>', views.gestionarSectorEconomico),

    path('gestionar-certificados', views.gestionarGestCertificado),
    path('gestionar-certificados/', views.gestionarGestCertificado),
    path('gestionar-certificados/<str:idAux>', views.gestionarGestCertificado),

    path('gestionar-tematicas', views.gestionarTematica),
    path('gestionar-tematicas/', views.gestionarTematica),
    path('gestionar-tematicas/<str:idAux>', views.gestionarTematica),
    
]
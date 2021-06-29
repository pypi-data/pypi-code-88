from .common import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
MODO_SERVIDOR = 'PRUEBAS'
MICROSIP_VERSION = '2017'
EXTRA_MODULES = (
    # 'django-microsip-cancela-cfdi',
    # 'django-microsip-consolidador',
    # 'django-microsip-liquida',
    # 'django-microsip-quickbooks',
    # 'django-microsip-ventas-remgencargos',
    # 'django_microsip_catalogoarticulos',
    # 'django_microsip_catalogoprod',
    # 'django_microsip_consultaprecio',
    # 'django_microsip_diot',
    # 'django_microsip_exporta_xml',
    # 'django_microsip_exportaexcel',
    # 'django_msp_controldeacceso',
    # 'django_msp_facturaglobal',
    # 'django_msp_importa_inventario',
    # 'django_msp_sms',
    # 'djmicrosip_actualizarcosto',
    # 'djmicrosip_auditacotizacion',
    # 'djmicrosip_cambiaprecio_sincosto',
    # 'djmicrosip_cambiaprecios',
    # 'djmicrosip_cargos_cxp',
    # 'djmicrosip_cotizador',
    # 'djmicrosip_cotizadormovil',
    # 'djmicrosip_exportadb',
    # 'djmicrosip_exportaimportaprecios',
    # 'djmicrosip_faexist',
    # 'djmicrosip_facturacion',
    # 'djmicrosip_inventarios',
    # 'djmicrosip_mail',
    # 'djmicrosip_comparadb',
    # 'djmicrosip_mensajesdocumentos',
    # 'djmicrosip_organizador',
    # 'djmicrosip_polizas',
    # 'djmicrosip_polizasautomaticas',
    # 'djmicrosip_puntos',
    # 'djmicrosip_remgencargos',
    # 'djmicrosip_reorden',
    # 'djmicrosip_reportes',
    # 'djmicrosip_generareorden',
    # 'djmicrosip_generaventasconsig',
    # 'djmicrosip_tareas',
    # 'djmicrosip_traspasofacturas',
    # 'djmicrosip_utilerias',
    # 'djmicrosip_utilerias',
    # 'djmicrosip_generareorden',
)

DJANGO_APPS += (
    'django_extensions',
    'werkzeug_debugger_runserver',
)


from .common import get_microsip_extra_apps
MICROSIP_EXTRA_APPS, EXTRA_APPS = get_microsip_extra_apps(EXTRA_MODULES, is_dev=True)
INSTALLED_APPS = DJANGO_APPS + MICROSIP_MODULES + MICROSIP_EXTRA_APPS

ROOT_URLCONF = 'django_microsip_base.urls.dev'

# Additional locations of static files
STATICFILES_DIRS = (
    (BASE_DIR + '/static/'),
)

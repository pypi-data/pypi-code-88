#encoding:utf-8
from django.db import models
from django.db import router
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from microsip_api.comun.sic_db import next_id, first_or_none
import django.dispatch
articulo_clave_save_signal = django.dispatch.Signal()
plazo_condicion_pago_save_signal = django.dispatch.Signal()

from microsip_api.models_base.comun.articulos import *
from microsip_api.models_base.comun.catalogos import *
from microsip_api.models_base.comun.clientes import *
from microsip_api.models_base.comun.listas import *
from microsip_api.models_base.comun.otros import *
from microsip_api.models_base.comun.proveedores import *
from microsip_api.models_base.comun.cfdi import *

from microsip_api.models_base.configuracion.folios_fiscales import *
from microsip_api.models_base.configuracion.preferencias import *

from microsip_api.models_base.punto_de_venta.documentos import *
from microsip_api.models_base.punto_de_venta.listas import *

from microsip_api.models_base.compras.documentos import *
from microsip_api.models_base.compras.otros import *

from microsip_api.models_base.cuentas_por_pagar.documentos import *
from microsip_api.models_base.cuentas_por_pagar.catalogos import *

from microsip_api.models_base.cuentas_por_cobrar.documentos import *
from microsip_api.models_base.cuentas_por_cobrar.catalogos import *

from microsip_api.models_base.ventas.documentos import *

from microsip_api.models_base.inventarios.documentos import *
from microsip_api.models_base.inventarios.otros import *
from microsip_api.models_base.inventarios.catalogos import *

from microsip_api.models_base.contabilidad.documentos import *
from microsip_api.models_base.contabilidad.catalogos import *
from microsip_api.models_base.contabilidad.listas import *
from microsip_api.comun.comun_functions import split_letranumero

################################################################
####                                                        ####
####                        OTROS                           ####
####                                                        ####
################################################################


@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()

class DatabaseSucursal(models.Model):  
    name = models.CharField(max_length=100)
    empresa_conexion = models.CharField(max_length=200)
    sucursal_conexion = models.CharField(max_length=200)
    sucursal_conexion_name = models.CharField(max_length=200)
    
    def __str__(self):  
          return self.name    
          
    class Meta:
        app_label =u'auth'

class ConexionDB(models.Model):  
    nombre = models.CharField(max_length=100)
    TIPOS = (('L', 'Local'),('R', 'Remota'),)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    servidor = models.CharField(max_length=250)
    carpeta_datos = models.CharField(max_length=300)
    usuario = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    def __str__(self):  
          return self.nombre    
          
    class Meta:
        app_label =u'auth' 

class AplicationPlugin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    
    def __unicode__(self):
        return u'%s' % self.nombre

    class Meta:
        app_label =u'auth'
        db_table = u'sic_aplicationplugin'

class SaldosSms(models.Model):
    id = models.AutoField(primary_key=True,db_column='ID_SIC_SMS_SALDO')
    tipo=models.CharField(max_length=1, db_column='TIPO')
    cliente=models.ForeignKey('Cliente', blank=True, null=True , db_column='CLIENTE_ID',on_delete=models.CASCADE)
    cantidad=models.IntegerField(blank=True, null=True, db_column='CANTIDAD')
    fecha=models.DateTimeField(auto_now=True, blank=True, null=True, db_column='FECHA')
    persona_solicito=models.CharField(max_length=200, db_column='PERSONA_SOLICITO')
    archivo = models.FileField(blank=True, null=True , upload_to='llaves', db_column='ARCHIVO')

    class Meta:
        db_table = u'sic_sms_saldos'
        app_label='models_base'



################################################################
####                                                        ####
####                        CONFIGURACION                   ####
####                                                        ####
################################################################

# PREFERENCIAS

class Registry(RegistryBase):
    pass


class RegistryLong(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    valor = models.TextField()
    
    class Meta:
        db_table = u'SIC_REGISTRY'
        managed=False

#FOLIOS FISCALES

class ConfiguracionFolioFiscal(ConfiguracionFolioFiscalBase): 
    pass

class ConfiguracionFolioFiscalUso(ConfiguracionFolioFiscalUsoBase):
    pass

################################################################
####                                                        ####
####                        COMUN                           ####
####                                                        ####
################################################################

# OTROS
class ClaveGeneral(ClaveGeneralBase):
    pass
    
class Pais(PaisBase):
    def save(self, *args, **kwargs):    
        kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
        if self.id == None:
            self.id = next_id('ID_CATALOGOS', kwargs['using'])

        super(self.__class__, self).save(*args, **kwargs)
        
        if self.es_predet == 'S':
            Pais.objects.using(kwargs['using']).all().exclude(pk=self.id).update(es_predet='N')

    
class Estado(EstadoBase):
    def save(self, *args, **kwargs):
        kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
        if self.id == None:
            self.id = next_id('ID_CATALOGOS', kwargs['using'])

        super(self.__class__, self).save(*args, **kwargs)
        
        if self.es_predet == 'S':
            Estado.objects.using(kwargs['using']).all().exclude(pk=self.id).update(es_predet='N')


class Ciudad(CiudadBase):
    def save(self, *args, **kwargs):
        kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
        if self.id == None:
            self.id = next_id('ID_CATALOGOS', kwargs['using'])
            
        super(self.__class__, self).save(*args, **kwargs)
        
        if self.es_predet == 'S':
            Ciudad.objects.using(kwargs['using']).all().exclude(pk=self.id).update(es_predet='N')


class Moneda(MonedaBase):
    pass

class TipoCambio(TipoCambioBase):
    pass

class Atributo(AtributoBase):
    pass

class AtributoLista(AtributoListaBase):
    pass
    
class ViaEmbarque(ViaEmbarqueBase):
   pass

class FolioVenta(FolioVentaBase):
    pass

class FolioCompra(FolioCompraBase):
    pass

# ARTICULOS

class GrupoLineas(GrupoLineasBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_puntos.djmicrosip_puntos' in settings.INSTALLED_APPS or 'djmicrosip_puntos' in settings.INSTALLED_APPS:
        puntos = models.IntegerField(blank=True, null=True, db_column='SIC_PUNTOS')
        dinero_electronico = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DINERO_ELECTRONICO')

class LineaArticulos(LineaArticulosBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_puntos.djmicrosip_puntos' in settings.INSTALLED_APPS or 'djmicrosip_puntos' in settings.INSTALLED_APPS:
        puntos = models.IntegerField(blank=True, null=True, db_column='SIC_PUNTOS')
        dinero_electronico = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DINERO_ELECTRONICO')
        hereda_puntos = models.BooleanField( db_column='SIC_HEREDA_PUNTOS')

class Articulo(ArticuloBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_puntos.djmicrosip_puntos' in settings.INSTALLED_APPS or 'djmicrosip_puntos' in settings.INSTALLED_APPS:
        puntos = models.IntegerField(default = 0, blank = True, null = True, db_column = 'SIC_PUNTOS' )
        dinero_electronico  = models.DecimalField( default = 0, blank = True, null = True, max_digits = 15, decimal_places = 2, db_column = 'SIC_DINERO_ELECTRONICO' )
        hereda_puntos = models.BooleanField( db_column = 'SIC_HEREDA_PUNTOS' )

    if 'django_microsip_base.apps.plugins.django_microsip_catalogoarticulos.django_microsip_catalogoarticulos' in settings.INSTALLED_APPS or 'django_microsip_catalogoarticulos' in settings.INSTALLED_APPS:
        imagen = models.ImageField(blank=True, null=True , upload_to='articulos', db_column='SIC_IMAGEN_URL')

    if 'django_microsip_base.apps.plugins.djmicrosip_organizador.djmicrosip_organizador' in settings.INSTALLED_APPS or 'djmicrosip_organizador' in settings.INSTALLED_APPS:
        carpeta = models.ForeignKey('Carpeta', blank=True, null=True , db_column='SIC_CARPETA_ID',on_delete=models.CASCADE)

    if 'django_microsip_base.apps.plugins.djmicrosip_faexist.djmicrosip_faexist' in settings.INSTALLED_APPS or 'djmicrosip_faexist' in settings.INSTALLED_APPS:
        facturaexistencia_ignorar = models.BooleanField( db_column = 'SIC_FAEXIST_IGNORAR' )

class ArticuloClaveRol(ArticuloClaveRolBase):
    pass

class ArticuloClave(ArticuloClaveBase):
    def save_send_signal(self, *args, **kwargs):
        articulo_clave_save_signal.send(sender=self, *args, **kwargs)

class ArticuloPrecio(ArticuloPrecioBase):
    pass

class Almacen(AlmacenBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_inventarios.djmicrosip_inventarios' in settings.INSTALLED_APPS or 'djmicrosip_inventarios' in settings.INSTALLED_APPS:
        inventariando = models.BooleanField(default= False, db_column = 'SIC_INVENTARIANDO' )
        inventario_conajustes = models.BooleanField(default= False, db_column = 'SIC_INVCONAJUSTES' )
        inventario_modifcostos = models.BooleanField(default= False, db_column = 'SIC_INVMODIFCOSTOS' )

class PrecioEmpresa(PrecioEmpresaBase):
    pass

class ArticuloDiscreto(ArticuloDiscretoBase):
    pass

class ArticuloDiscretoExistencia(ArticuloDiscretoExistenciaBase):
    pass

class ArticuloNivel(ArticuloNivelBase):
    pass

class Banco(BancoBase):
    pass  

class Clasificadores(ClasificadoresBase):
    pass

class ClasificadoresValores(ClasificadoresValoresBase):
    pass

class ElementosClasificadores(ElementosClasificadoresBase):
    pass
    
#CATALOGOS

class Banco(BancoBase):
    pass

# LISTAS

class ImpuestoTipo(ImpuestoTipoBase):
    pass

class Impuesto(ImpuestoBase):
    def save(self, *args, **kwargs):    
        kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
        super(self.__class__, self).save(*args, **kwargs)

        if self.es_predet == 'S':
            Impuesto.objects.using(kwargs['using']).all().exclude(pk=self.id).update(es_predet='N')


class ImpuestosArticulo(ImpuestoArticuloBase):
    pass

class Vendedor(VendedorBase):
    pass


# CLIENTES

class ClienteTipo(ClienteTipoBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_puntos.djmicrosip_puntos' in settings.INSTALLED_APPS or 'djmicrosip_puntos' in settings.INSTALLED_APPS:
        valor_puntos = models.DecimalField( default = 0, blank = True, null = True, max_digits = 15, decimal_places = 2, db_column = 'SIC_VALOR_PUNTOS' )

class CondicionPago(CondicionPagoBase):
    def save(self, *args, **kwargs):    
        kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
        super(self.__class__, self).save(*args, **kwargs)

        if self.es_predet == 'S':
            CondicionPago.objects.using(kwargs['using']).all().exclude(pk=self.id).update(es_predet='N')


class CondicionPagoPlazo(CondicionPagoPlazoBase):
    def save_send_signal(self, *args, **kwargs):
        articulo_clave_save_signal.send(sender=self, *args, **kwargs)

class Cliente(ClienteBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_puntos.djmicrosip_puntos' in settings.INSTALLED_APPS or 'djmicrosip_puntos' in settings.INSTALLED_APPS:
        TIPOS = ( ( 'N', 'No Aplica' ),( 'D', 'Dinero Electronico' ), ) #( 'P', 'Puntos' ),
        tipo_tarjeta = models.CharField( default = 'N', max_length = 1, choices = TIPOS, db_column = 'SIC_TIPO_TARJETA' )
        hereda_valorpuntos = models.BooleanField( db_column = 'SIC_HEREDA_VALORPUNTOS' )
        valor_puntos = models.DecimalField( default = 0, blank = True, null = True, max_digits = 15, decimal_places = 2, db_column = 'SIC_VALOR_PUNTOS' )
        hereda_puntos_a = models.ForeignKey( 'self', db_column = 'SIC_HEREDAR_PUNTOS_A', related_name = 'hereda_puntos_a_cliente', blank = True, null = True ,on_delete=models.CASCADE)
        vigencia_fecha_inicio = models.DateField(blank=True, null=True, db_column='SIC_PUNTOS_VIGENCIA_INICIO')
        vigencia_fecha_fin = models.DateField(blank=True, null=True, db_column='SIC_PUNTOS_VIGENCIA_FIN')
        # fecha_corte = models.DateField(blank=True, null=True, db_column='SIC_FECHA_CORTE')
        aplicar_descuento_sin_tarjeta = models.BooleanField( db_column = 'SIC_APLICAR_DSCTO' )
    if 'django_microsip_base.apps.plugins.django_msp_sms.django_msp_sms' in settings.INSTALLED_APPS or 'django_msp_sms' in settings.INSTALLED_APPS:
        no_enviar_sms = models.BooleanField( db_column = 'SIC_SMS_NOENVIAR' )
    if 'django_microsip_base.apps.plugins.djmicrosip_mail.djmicrosip_mail' in settings.INSTALLED_APPS or 'djmicrosip_mail' in settings.INSTALLED_APPS:
        no_enviar_mail = models.BooleanField( db_column = 'SIC_MAIL_NOENVIAR' )
    if 'django_microsip_base.apps.plugins.django_msp_controldeacceso.django_msp_controldeacceso' in settings.INSTALLED_APPS or 'django_msp_controldeacceso' in settings.INSTALLED_APPS:
        imagen = models.ImageField(blank=True, null=True , upload_to='clientes', db_column='SIC_IMAGEN_URL')

class Zona(ZonaBase):
    pass
    
class ClienteClaveRol(ClienteClaveRolBase):
    pass

class ClienteClave(ClienteClaveBase):
    pass

class ClienteDireccion(ClienteDireccionBase):
    pass

class LibresClientes(LibreClienteBase):

    if (('django_microsip_base.apps.plugins.djmicrosip_polizas.djmicrosip_polizas' in settings.INSTALLED_APPS or 'djmicrosip_polizas' in settings.INSTALLED_APPS) or 
        ('django_microsip_base.apps.plugins.djmicrosip_exportadb.djmicrosip_exportadb' in settings.INSTALLED_APPS or 'djmicrosip_exportadb' in settings.INSTALLED_APPS)):
        cuenta_1 = models.CharField(max_length=99, db_column='CUENTA_1')
        cuenta_2 = models.CharField(max_length=99, db_column='CUENTA_2')
    
# PROVEEDORES

class ProveedorTipo(ProveedorTipoBase):
    pass
        
class Proveedor(ProveedorBase):
    pass 
    
################################################################
####                                                        ####
####                      COMPRAS                           ####
####                                                        ####
################################################################

# OTROS

class Aduana(AduanaBase):
    pass

class Pedimento(PedimentoBase):
    pass

class DesglosePedimento(DesglosePedimentoBase):
    pass

class PedimentoCapa(PedimentoCapaBase):
    pass

class PedimentoCapaUso(PedimentoCapaUsoBase):
    pass
    
# DOCUMENTOS

class ComprasConsignatario(ComprasConsignatarioBase):
    pass

class ComprasDocumento(ComprasDocumentoBase):
    def next_folio( self, connection_name=None, **kwargs ):
        ''' Funcion para generar el siguiente folio de un documento de ventas '''
        #Parametros opcionales
        serie = kwargs.get('serie', None)
        consecutivos_folios = FolioCompra.objects.using(connection_name).filter(tipo_doc = self.tipo)
        if serie:
            consecutivos_folios = consecutivos_folios.filter(serie=serie)

        consecutivo_row = first_or_none(consecutivos_folios)
        consecutivo = ''
        if consecutivo_row:
            consecutivo = consecutivo_row.consecutivo 
            serie = consecutivo_row.serie
            if serie == u'@':
                serie = ''
                
        folio = '%s%s'% (serie,("%09d" % int(consecutivo))[len(serie):]) 

        consecutivo_row.consecutivo = consecutivo_row.consecutivo + 1
        consecutivo_row.save(using=connection_name)
        return folio

    def save(self, *args, **kwargs):
        if self.folio == '':
            kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
            self.folio = self.next_folio(connection_name=kwargs['using'])

        super(self.__class__, self).save(*args, **kwargs)

class ComprasDocumentoCargoVencimiento(ComprasDocumentoCargoVencimientoBase):
    pass

class ComprasDocumentoDetalle(ComprasDocumentoDetalleBase):
    pass

class ComprasDocumentoImpuesto(ComprasDocumentoImpuestoBase):
    pass

class ComprasDocumentoLiga(ComprasDocumentoLigaBase):
    pass

class ComprasDocumentoLigaDetalle(ComprasDocumentoLigaDetalleBase):
    pass


#####################################################
##
##                         INVENTARIOS
##
##
#####################################################

# CATALOGOS

class InventariosConcepto(InventariosConceptoBase):
    pass

class InventariosCentroCostos(InventariosCentroCostosBase):
    pass

#  DOCUMENTOS

class InventariosDocumento(InventariosDocumentoBase):

    def next_folio( self, connection_name=None):
        ''' Funcion para generar el siguiente folio de un documento inventario '''

        folio = ''
        concepto_in = self.concepto
        if concepto_in.folio_autom and concepto_in.sig_folio:
            serie, folio_numero = split_letranumero(concepto_in.sig_folio)
            folio = '%s%s' % (serie, ("%09d" % int(folio_numero))[len(serie):])

            # generamos el nuevo folio
            folio_numero = int(folio_numero)+1
            sig_folio = '%s%s' % (serie, ("%09d" % int(folio_numero))[len(serie):])
        concepto_in.sig_folio = sig_folio
        concepto_in.save()

        return folio

    def save(self, *args, **kwargs):
        if not self.folio and self.concepto.folio_autom == 'S':
            kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
            self.folio = self.next_folio()

        super(self.__class__, self).save(*args, **kwargs)


class InventariosDocumentoDetalle(InventariosDocumentoDetalleBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_inventarios.djmicrosip_inventarios' in settings.INSTALLED_APPS or 'djmicrosip_inventarios' in settings.INSTALLED_APPS:
        fechahora_ult_modif = models.DateTimeField(auto_now=True, blank=True, null=True, db_column='SIC_FECHAHORA_U')
        usuario_ult_modif = models.CharField(blank=True, null=True, max_length=31, db_column='SIC_USUARIO_ULT_MODIF')
        detalle_modificacionestime = models.CharField(blank=True, null=True, max_length=400, db_column='SIC_DETALLETIME_MODIFICACIONES')

class InventariosDocumentoIF(InventariosDocumentoIFBase):
    pass

class InventariosDocumentoIFDetalle(InventariosDocumentoIFDetalleBase):
    pass

# OTROS

class InventariosDesgloseEnDiscretos(InventariosDesgloseEnDiscretosBase):
    pass

class InventariosDesgloseEnDiscretosIF(InventariosDesgloseEnDiscretosIFBase):
    pass


################################################################
####                                                        ####
####               MODELOS CUENTAS POR PAGAR                ####
####                                                        ####
################################################################

# CATALOGOS

class CuentasXPagarConcepto(CuentasXPagarConceptoBase):
    pass

class CuentasXPagarCondicionPago(CuentasXPagarCondicionPagoBase):
    pass

class CuentasXPagarCondicionPagoPlazo(CuentasXPagarCondicionPagoPlazoBase):
    pass

# DOCUMENTOS

class CuentasXPagarDocumento(CuentasXPagarDocumentoBase):
    pass
class CuentasXPagarDocumentoImportes(CuentasXPagarDocumentoImportesBase):
   pass

class CuentasXPagarDocumentoImportesImpuesto(CuentasXPagarDocumentoImportesImpuestoBase):
    pass

class CuentasXPagarDocumentoCargoLibres(CuentasXPagarDocumentoCargoLibresBase):
    pass

################################################################
####                                                        ####
####               MODELOS CUENTAS POR COBRAR               ####
####                                                        ####
################################################################

# CATALOGOS

class CuentasXCobrarConcepto(CuentasXCobrarConceptoBase):
    pass

# DOCUMENTOS

class CuentasXCobrarDocumento(CuentasXCobrarDocumentoBase):
    pass

class CuentasXCobrarDocumentoImportes(CuentasXCobrarDocumentoImportesBase):
    pass

class CuentasXCobrarDocumentoImportesImpuesto(CuentasXCobrarDocumentoImportesImpuestoBase): 
    pass
    
class CuentasXCobrarDocumentoCargoVencimiento(CuentasXCobrarDocumentoCargoVencimientoBase):
    pass

class CuentasXCobrarDocumentoCargoLibres(CuentasXCobrarDocumentoCargoLibresBase):
    pass

class CuentasXCobrarDocumentoCreditoLibres(CuentasXCobrarDocumentoCreditoLibresBase):
    pass

################################################################
####                                                        ####
####               MODELOS CONTABILIDAD                     ####
####                                                        ####
################################################################

# CATALOGOS

class ContabilidadCuentaContable(ContabilidadCuentaContableBase):
    pass

# DOCUMENTOS

class ContabilidadGrupoPolizaPeriodo(ContabilidadGrupoPolizaPeriodoBase):
    pass

class ContabilidadRecordatorio(ContabilidadRecordatorioBase):
    pass

class ContabilidadDocumento(ContabilidadDocumentoBase):
    def next_folio( self, using=None):
        """ Generar un folio nuevo de una poliza e incrementa el consecutivo de folios """
        tipo_poliza = self.tipo_poliza
        prefijo = tipo_poliza.prefijo
        if not prefijo:
            prefijo = ''
        tipo_consecutivo = tipo_poliza.tipo_consec

        try:
            if tipo_consecutivo == 'M':
                tipo_poliza_det = TipoPolizaDetalle.objects.get(tipo_poliza = tipo_poliza, mes= self.fecha.month, ano = self.fecha.year)
            elif tipo_consecutivo == 'E':
                tipo_poliza_det = TipoPolizaDetalle.objects.get(tipo_poliza = tipo_poliza, ano=self.fecha.year, mes=0)
            elif tipo_consecutivo == 'P':
                tipo_poliza_det = TipoPolizaDetalle.objects.get(tipo_poliza = tipo_poliza, mes=0, ano =0)
        except ObjectDoesNotExist:
            if tipo_consecutivo == 'M':      
                tipo_poliza_det = TipoPolizaDetalle.objects.create(id=next_id('ID_CATALOGOS', using), tipo_poliza=tipo_poliza, ano=self.fecha.year, mes=self.fecha.month, consecutivo = 1,)
            elif tipo_consecutivo == 'E':
                #Si existe permanente toma su consecutivo para crear uno nuevo si no existe inicia en 1
                consecutivo = TipoPolizaDetalle.objects.filter(tipo_poliza = tipo_poliza, mes=0, ano =0).aggregate(max = Sum('consecutivo'))['max']

                if consecutivo == None:
                    consecutivo = 1

                tipo_poliza_det = TipoPolizaDetalle.objects.create(id=next_id('ID_CATALOGOS', using), tipo_poliza=tipo_poliza, ano= self.fecha.year, mes=0, consecutivo=consecutivo,)
            elif tipo_consecutivo == 'P':
                consecutivo = TipoPolizaDetalle.objects.all().aggregate(max = Sum('consecutivo'))['max']

                if consecutivo == None:
                    consecutivo = 1

                tipo_poliza_det = TipoPolizaDetalle.objects.create(id=next_id('ID_CATALOGOS', using), tipo_poliza=tipo_poliza, ano=0, mes=0, consecutivo = consecutivo,)                                
        
        folio = '%s%s'% (prefijo,("%09d" % tipo_poliza_det.consecutivo)[len(prefijo):]) 

        #CONSECUTIVO DE FOLIO DE POLIZA
        tipo_poliza_det.consecutivo += 1 
        tipo_poliza_det.save()
        
        return folio
    
    def save(self, *args, **kwargs):
        
        if not self.poliza:
            kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
            self.poliza = self.next_folio(using=kwargs['using'])

        super(self.__class__, self).save(*args, **kwargs)

    if 'django_microsip_base.apps.plugins.djmicrosip_polizasautomaticas.djmicrosip_polizasautomaticas' in settings.INSTALLED_APPS or 'djmicrosip_polizasautomaticas' in settings.INSTALLED_APPS:
        sic_referencia = models.CharField(blank=True, null=True, max_length=400, db_column='SIC_POLIZASAUTO_REF')
   

class ContabilidadDocumentoDetalle(ContabilidadDocumentoDetalleBase):
    pass

class ContabilidadPoliza(ContabilidadPolizaBase):
    pass
# LISTAS

class TipoPoliza(TipoPolizaBase):
    pass

class TipoPolizaDetalle(TipoPolizaDetalleBase):
    pass

class ContabilidadDepartamento(ContabilidadDepartamentoBase):
    pass

################################################################
####                                                        ####
####                    MODELOS VENTAS                      ####
####                                                        ####
################################################################

# DOCUMENTOS
class VentasDocumento(VentasDocumentoBase):
    
    def next_folio( self, connection_name=None, **kwargs ):
        ''' Funcion para generar el siguiente folio de un documento de ventas '''

        #Parametros opcionales
        serie = kwargs.get('serie', None)

        if self.tipo in ('P', 'R'):
            consecutivos_folios = FolioVenta.objects.using(connection_name).filter(tipo_doc = self.tipo)
            if serie:
                consecutivos_folios = consecutivos_folios.filter(serie=serie)

            consecutivo_row = first_or_none(consecutivos_folios)
            consecutivo = ''
            if consecutivo_row:
                consecutivo = consecutivo_row.consecutivo 
                serie = consecutivo_row.serie
            consecutivo_row.consecutivo = consecutivo_row.consecutivo + 1

        elif self.tipo == 'F':
            consecutivos_folios = FolioVenta.objects.using(connection_name).filter(tipo_doc = self.tipo, modalidad_facturacion = self.modalidad_facturacion)
            if serie:
                consecutivos_folios = consecutivos_folios.filter(serie=serie)

            consecutivo_row = first_or_none(consecutivos_folios)
            consecutivo = ''
            if consecutivo_row: 
                consecutivo = consecutivo_row.consecutivo 
                serie = consecutivo_row.serie
                if serie == u'@':
                    serie = ''
            consecutivo_row.consecutivo = consecutivo_row.consecutivo + 1
        elif self.tipo == 'S':
            consecutivos_folios=Registry.objects.get( nombre = 'SIC_Pedidos_Crm_Url_Consecutivo_Solicitud').get_value()
            consecutivo_row=Registry.objects.get( nombre = 'SIC_Pedidos_Crm_Url_Consecutivo_Solicitud')
            serie='S'
            consecutivo = int(consecutivos_folios) + 1
            consecutivo_row.valor=str(consecutivo)
            print(consecutivo)


        folio = '%s%s'% (serie,("%09d" % int(consecutivo))[len(serie):]) 
        print("******",folio)
        
        consecutivo_row.save(using=connection_name)

        return folio, consecutivo

    def save(self, *args, **kwargs):
        kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))

        consecutivo = ''
        #Si no se define folio se asigna uno
        if self.folio == '':
            self.folio, consecutivo = self.next_folio(connection_name=kwargs['using'])

        super(self.__class__, self).save(*args, **kwargs)

        #si es factura 
        if consecutivo != '' and self.tipo == 'F' and self.modalidad_facturacion == 'CFDI':
            folios_fiscales = first_or_none(ConfiguracionFolioFiscal.objects.using(kwargs['using']).filter(modalidad_facturacion=self.modalidad_facturacion))
            if not folios_fiscales:
                ConfiguracionFolioFiscal.objects.using(kwargs['using']).create(
                        serie = '@',
                        folio_ini = 1,
                        folio_fin = 999999999,
                        ultimo_utilizado = 0,
                        num_aprobacion ="1",
                        ano_aprobacion = 1,
                        modalidad_facturacion = self.modalidad_facturacion,
                    )
                folios_fiscales = first_or_none(ConfiguracionFolioFiscal.objects.using(kwargs['using']).filter(modalidad_facturacion=self.modalidad_facturacion))

            if folios_fiscales:
                ConfiguracionFolioFiscalUso.objects.using(kwargs['using']).create(
                        id= -1,
                        folios_fiscales = folios_fiscales,
                        folio= consecutivo,
                        fecha = datetime.now(),
                        sistema = self.sistema_origen,
                        documento = self.id,
                        xml = '',
                    )


class VentasDocumentoVencimiento(VentasDocumentoVencimientoBase):
    pass

class VentasDocumentoImpuesto(VentasDocumentoImpuestoBase):
    pass


class VentasDocumentoDetalle(VentasDocumentoDetalleBase):
    pass

class VentasDocumentoLiga(VentasDocumentoLigaBase):
    pass

class VentasDocumentoFacturaLibres(VentasDocumentoFacturaLibresBase):
    pass
    
class VentasDocumentoFacturaDevLibres(VentasDocumentoFacturaDevLibresBase):
    pass

################################################################
####                                                        ####
####                MODELOS PUNTO DE VENTAS                 ####
####                                                        ####
################################################################

#LISTAS

class Cajero(CajeroBase):
    pass

class Caja(CajaBase):
    pass 

class CajaFolios(CajaFoliosBase):
    pass 

class CajeroCaja(CajeroCajaBase):
    pass

class FormaCobro(FormaCobroBase):
    pass

class FormaCobroReferencia(FormaCobroReferenciaBase):
    pass

class CajaMovimiento(CajaMovimientoBase):
    pass

class CajaMovimientoFondo(CajaMovimientoFondoBase):
    pass

#DOCUMENTOS

class PuntoVentaDocumento(PuntoVentaDocumentoBase): 
    if 'django_microsip_base.apps.plugins.djmicrosip_puntos.djmicrosip_puntos' in settings.INSTALLED_APPS or 'djmicrosip_puntos' in settings.INSTALLED_APPS:
        puntos                  = models.IntegerField(db_column='SIC_PUNTOS')
        dinero_electronico      = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DINERO_ELECTRONICO')
        cliente_tarjeta = models.ForeignKey(Cliente, db_column='sic_cliente_tarjeta',  related_name='cliente_tarjeta', blank=True, null=True,on_delete=models.CASCADE)
        puntos_pago = models.IntegerField(default=0, db_column='SIC_PUNTOS_PAGO')
        dinero_electronico_pago = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DINERO_ELECTRONICO_PAGO')
        dinero_a_descontar = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DINEROADESCONTAR')
    # if 'django_microsip_base.apps.plugins.django_msp_facturaglobal.django_msp_facturaglobal' in settings.INSTALLED_APPS or 'django_msp_facturaglobal' in settings.INSTALLED_APPS:
    #     tipo_gen_fac = models.CharField(default='N',blank=True, null=True, max_length=1, db_column='TIPO_GEN_FAC')
    #     es_fac_global = models.CharField(default='N', blank=True, null=True, max_length=1, db_column='ES_FAC_GLOBAL')
    #     fecha_ini_fac_global = models.DateField(blank=True, null=True, db_column='FECHA_INI_FAC_GLOBAL')
    #     fecha_fin_fac_global = models.DateField(blank=True, null=True, db_column='FECHA_FIN_FAC_GLOBAL')

    def next_folio( self, connection_name=None, **kwargs ):
        ''' Funcion para generar el siguiente folio de un documento de ventas '''
        
        #Parametros opcionales
        serie = kwargs.get('serie', None)
        
        if self.tipo == 'F':
            consecutivos_folios = FolioVenta.objects.using(connection_name).filter(tipo_doc = self.tipo, modalidad_facturacion = self.modalidad_facturacion)
            if serie:
                consecutivos_folios = consecutivos_folios.filter(serie=serie)

            consecutivo_row = first_or_none(consecutivos_folios)
            consecutivo = ''
            if consecutivo_row:
                consecutivo = consecutivo_row.consecutivo 
                serie = consecutivo_row.serie
                if serie == u'@':
                    serie = ''

            consecutivo_row.consecutivo = consecutivo_row.consecutivo + 1
            consecutivo_row.save()

        elif self.tipo == 'V' or self.tipo == 'O':
            caja_folios_list =  CajaFolios.objects.filter(caja= self.caja, documento_tipo = self.tipo).values_list( 'serie', 'consecutivo')[0]
            serie = caja_folios_list[0]
            consecutivo = caja_folios_list[1]
            c = connections[connection_name].cursor()
            
            #codigo para checar si el folio no esta ya indicado en un documento
            folio_correcto = False
            while not folio_correcto:
                folio = '%s%s'% (serie,("%09d" % int(consecutivo))[len(serie):]) 
                query = "select count(*) from DOCTOS_PV where FOLIO='%s' AND TIPO_DOCTO='%s'"%(folio,self.tipo)
    
                c.execute(query)
                documentos_con_folio = c.fetchall()[0][0]
                if documentos_con_folio == 0:
                    folio_correcto = True
                else:
                    consecutivo = consecutivo + 1

            query = '''UPDATE FOLIOS_CAJAS set CONSECUTIVO=%s WHERE CAJA_ID = %s and TIPO_DOCTO = %s;'''
            c.execute(query,[consecutivo+1, self.caja.id, self.tipo])
            c.close()

        folio = '%s%s'% (serie,("%09d" % int(consecutivo))[len(serie):]) 

        return folio, consecutivo - 1

    def save(self, *args, **kwargs):
        kwargs['using'] = kwargs.get('using', router.db_for_write(self.__class__, instance=self))
        
        consecutivo = ''
        fo = self.folio
        #Si no se define folio se asigna uno
        if self.folio == '':
            self.folio, consecutivo = self.next_folio(connection_name=kwargs['using'])

        super(self.__class__, self).save(*args, **kwargs)
        
        #si es factura 
        if consecutivo != '' and self.tipo == 'F' and self.modalidad_facturacion == 'CFDI':
            folios_fiscales = first_or_none(ConfiguracionFolioFiscal.objects.using(kwargs['using']).filter(modalidad_facturacion=self.modalidad_facturacion))
            if folios_fiscales:
                ConfiguracionFolioFiscalUso.objects.using(kwargs['using']).create(
                        id= -1,
                        folios_fiscales = folios_fiscales,
                        folio= consecutivo,
                        fecha = datetime.now(),
                        sistema = self.sistema_origen,
                        documento = self.id,
                        xml = '',
                    )


class PuntoVentaDocumentoDetalle(PuntoVentaDocumentoDetalleBase):
    if 'django_microsip_base.apps.plugins.djmicrosip_puntos.djmicrosip_puntos' in settings.INSTALLED_APPS or 'djmicrosip_puntos' in settings.INSTALLED_APPS:
        puntos                  = models.IntegerField(db_column='SIC_PUNTOS')
        dinero_electronico      = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DINERO_ELECTRONICO')

class PuntoVentaDocumentoLiga(PuntoVentaDocumentoLigaBase):
   pass

class PuntoVentaDocumentoLigaDetalle(PuntoVentaDocumentoLigaDetalleBase):
    pass

class PuntoVentaDocumentoDetalleTransferencia(PuntoVentaDocumentoDetalleTransferenciaBase):
    pass

class PuntoVentaCobro(PuntoVentaCobroBase):
    pass

class PuntoVentaCobroReferencia(PuntoVentaCobroReferenciaBase):
    pass

class PuntoVentaDocumentoImpuesto(PuntoVentaDocumentoImpuestoBase):
    pass

class PuntoVentaDocumentoImpuestoGravado(PuntoVentaDocumentoImpuestoGravadoBase):
    pass

class PuntoVentaArticuloDiscreto(PuntoVentaArticuloDiscretoBase):
    pass
################################################################
####                                                        ####
####                        NOMINA                          ####
####                                                        ####
################################################################
from microsip_api.models_base.nomina.catalogos import *
from microsip_api.models_base.nomina.listas import *
from microsip_api.models_base.nomina.movimientos import *
from microsip_api.models_base.nomina.nominas import *

#Catalogos
class NominaEmpleado(NominaEmpleadoBase):
    pass

class NominaFrecuenciaPago(NominaFrecuenciaPagoBase):
    pass

class NominaConcepto(NominaConceptoBase):
    pass

#listas
class NominaTablaTipo(NominaTablaTipoBase):
    pass

class NominaTabla(NominaTablaBase):
    pass

#movimientos
class NominaPrestamo(NominaPrestamoBase):
    pass

#Nominas
class NominaNomina(NominaNominaBase):
    pass

class NominaNominaPago(NominaNominaPagoBase):
    pass

class NominaNominaPagoDetalle(NominaNominaPagoDetalleBase):
    pass


class Carpeta(models.Model):
    nombre  = models.CharField(max_length=50)
    carpeta_padre = models.ForeignKey('self', related_name='carpeta_padre_a', blank=True, null=True,on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s'% self.nombre

    class Meta:
        db_table = u'sic_carpeta'

# CFDI#######
class RepositorioCFDI(RepositorioCFDIBase):
    if 'django_microsip_base.apps.plugins.django_microsip_diot.django_microsip_diot' in settings.INSTALLED_APPS or 'django_microsip_diot' in settings.INSTALLED_APPS:
        diot_integrar = models.CharField(max_length=1,db_column='SIC_DIOT_INTEGRAR')
        diot_pagado = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DIOT_PAGADO')
        diot_mostrar = models.CharField(max_length=1,db_column='SIC_DIOT_MOSTRAR')
        diot_iva = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DIOT_IVA')
        diot_iva_retenido = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DIOT_IVA_RETENIDO')
        diot_iva_pagado = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DIOT_IVA_PAGADO')
        diot_iva_descuentos = models.DecimalField(default=0, blank=True, null=True, max_digits=15, decimal_places=2, db_column='SIC_DIOT_IVA_DESCUENTOS')
        diot_genero_ext = models.CharField(max_length=1,db_column='SIC_DIOT_GENERO_EXT')
        diot_proveedor_revisado = models.CharField(default='N', max_length=1, db_column='SIC_DIOT_PROVEEDOR_REVISADO')


class Log(models.Model):
    """Modelo para bitacora de errores generales"""
    app = models.CharField(max_length=40)
    message = models.TextField(max_length=40)
    creation = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.id

    class Meta:
        db_table = u'SIC_LOG'
        managed=False

class ClienteUsuario(models.Model):
    id=models.AutoField(primary_key=True, db_column='CLIENTE_USUARIO_ID')
    cliente=models.ForeignKey('Cliente', blank=True, null=True, db_column='CLIENTE_ID',on_delete=models.CASCADE)
    usuario=models.IntegerField(blank=True, null=True, db_column='USUARIO_ID')

    class Meta:
        db_table = 'SIC_CLIENTE_USUARIO'
        app_label = 'models_base'




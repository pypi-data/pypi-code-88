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
# from microsip_api.models_base.comun.articulos import *
# from microsip_api.models_base.comun.catalogos import *
from microsip_api.models_base.comun.clientes import *
# from microsip_api.models_base.comun.listas import *
# from microsip_api.models_base.comun.otros import *
# from microsip_api.models_base.comun.proveedores import *
# from microsip_api.models_base.comun.cfdi import *
from django_microsip_base.libs.models_base.models import Cliente

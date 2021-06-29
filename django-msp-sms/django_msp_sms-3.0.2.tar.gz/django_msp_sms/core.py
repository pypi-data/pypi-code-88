from django.db import router
from .models import *
from .config import configuration_registers, extrafields
from microsip_api.comun.comun_functions import exists_table_field


class InitialConfiguration(object):

    def __init__(self):
        self.errors = []
        self.is_valid = True
        self.IsValid()

    def IsValid(self):
        using = router.db_for_write(Cliente)
        self.is_valid = True

        # para validar que todos los registros existan
        for register in configuration_registers:
            if not Registry.objects.filter(nombre=register).exists():
                self.is_valid = False

        for extrafield in extrafields:
            table_name = extrafield[0]
            table_field = extrafield[1]
            if not exists_table_field(table_name, table_field, using):
                self.is_valid = False

        if self.is_valid is True:
            if Registry.objects.get(nombre='SIC_SMS_MontoMinimo').get_value() is None:
                self.is_valid = False

        if not self.is_valid:
            self.errors.append('''Por favor inicializa la configuracion de la aplicacion dando  <a href="/puntos/preferencias/actualizar_tablas/">click aqui</a>''')
            self.is_valid = False

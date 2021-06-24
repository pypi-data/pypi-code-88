from django.db.models import  CharField, BooleanField
from django.utils.translation import ugettext_lazy as _

from loducode_utils.models.audit import Audit


class City(Audit):
    STATES = (
        ('', '---------'),
        ('Amazonas', 'Amazonas'),
        ('Antioquia', 'Antioquia'),
        ('Arauca', 'Arauca'),
        ('Atlántico', 'Atlántico'),
        ('Bolívar', 'Bolívar'),
        ('Boyacá', 'Boyacá'),
        ('Caldas', 'Caldas'),
        ('Caquetá', 'Caquetá'),
        ('Casanare', 'Casanare'),
        ('Cauca', 'Cauca'),
        ('Cesar', 'Cesar'),
        ('Chocó', 'Chocó'),
        ('Córdoba', 'Córdoba'),
        ('Cundinamarca', 'Cundinamarca'),
        ('Guainía', 'Guainía'),
        ('Guaviare', 'Guaviare'),
        ('Huila', 'Huila'),
        ('La Guajira', 'La Guajira'),
        ('Magdalena', 'Magdalena'),
        ('Meta', 'Meta'),
        ('Nariño', 'Nariño'),
        ('Norte de Santander', 'Norte de Santander'),
        ('Putumayo', 'Putumayo'),
        ('Quindío', 'Quindío'),
        ('Risaralda', 'Risaralda'),
        ('San Andrés y Providencia', 'San Andrés y Providencia'),
        ('Santander', 'Santander'),
        ('Sucre', 'Sucre'),
        ('Tolima', 'Tolima'),
        ('Valle del Cauca', 'Valle del Cauca'),
        ('Vaupés', 'Vaupés'),
        ('Vichada', 'Vichada'),
        ('Bogotá d C.', 'Bogotá d C.'),
    )
    name: str = CharField(verbose_name=_('name'), max_length=100)
    state: str = CharField(verbose_name=_('departament'), max_length=100, choices=STATES)
    active: bool = BooleanField(verbose_name=_('active'),default=True)

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __str__(self):
        return f'{self.name} - {self.state}'
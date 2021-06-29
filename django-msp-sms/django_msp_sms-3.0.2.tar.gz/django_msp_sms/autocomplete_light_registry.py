from .models import *
from dal import autocomplete
from django.db.models import Q

autocomplete.register(Cliente,
                name='cliente-autocomplete',
                search_fields=('nombre',),
                choices= Cliente.objects.filter(Q(no_enviar_sms=None) | Q(no_enviar_sms=0)),
                autocomplete_js_attributes={ 'placeholder': 'Busca un cliente... ', },
                widget_js_attributes = {
                                        'max_values': 20,
                                        }
                )
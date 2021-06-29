from django_microsip_base.libs.models_base.models import Cliente, Articulo,Clasificadores,ClasificadoresValores,ElementosClasificadores,GrupoLineas,LineaArticulos
from autocomplete_light import shortcuts as autocomplete_light

autocomplete_light.register(Cliente, search_fields=('nombre','contacto1'), autocomplete_js_attributes={'placeholder': 'Cliente ..', 'class':'form-control',}, )
autocomplete_light.register(Articulo, search_fields=('nombre',), autocomplete_js_attributes={'placeholder': 'Articulo ..', 'class':'form-control',}, )
autocomplete_light.register(Clasificadores, search_fields=('nombre',), autocomplete_js_attributes={'placeholder': 'Clasificador ..', 'class':'form-control',}, )
autocomplete_light.register(ClasificadoresValores, search_fields=('valor',), autocomplete_js_attributes={'placeholder': 'Valor clasificadores ..', 'class':'form-control',}, )

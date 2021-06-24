from django.forms import widgets, fields
from samon.elements import BaseElement, AnonymusElement
from samon.constants import XML_NAMESPACE_DATA_BINDING
from samon.expressions import Bind
from samon.render import RenderedElement
from django_kirui.widgets import CheckboxSwitch


class RenderedField(RenderedElement):
    WIDGET_TO_TAG_MAPPER = {
        widgets.TextInput: 'kr-form-input',
        widgets.NumberInput: 'kr-number-input',
        widgets.Select: 'kr-form-select',
        widgets.CheckboxSelectMultiple: 'kr-multi-select-checkbox',
        widgets.CheckboxInput: 'kr-checkbox',
        CheckboxSwitch: 'kr-checkbox-switch',
    }

    def _eval_node_attributes(self, context) -> dict:
        retval = super(RenderedField, self)._eval_node_attributes(context)
        self.bf: fields.BoundField = retval.pop('boundField')

        if self.bf.field.initial:
            retval['value'] = self.bf.field.initial
        if self.bf.value():
            retval['value'] = self.bf.value()
        else:
            if self.bf.form.is_bound and self.bf.field.required:  # posted
                retval['value'] = None

        if self.bf.name in self.bf.form.errors.keys():
            retval['error'] = list(self.bf.form.errors[self.bf.name])[0]

        retval['widget'] = self.WIDGET_TO_TAG_MAPPER[self.bf.field.widget.__class__]
        retval['label'] = self.bf.field.label
        retval['required'] = self.bf.field.required
        retval['id'] = f'id_{self.bf.name}'
        retval['name'] = self.bf.name
        retval['onChange'] = f"{retval.pop('formReactContextRef')}.handleInputChange"

        return retval

    @property
    def children(self):
        if choices := getattr(self.bf.field, 'choices', None):
            value = self.node_attributes.get('value', None)
            for choice in choices:
                el = BaseElement(xml_tag='option', xml_attrs={})
                el.xml_attrs['value'] = str(choice[0])
                if isinstance(value, list) and el.xml_attrs['value'] in value:
                    el.xml_attrs['selected'] = True

                el.children = [AnonymusElement(choice[1])]
                yield RenderedElement(el, context=self._context)

        for child in super().children:
            yield child


class KrField(BaseElement):
    RENDERED_ELEMENT_CLASS = RenderedField
    TAG_NAME = 'kr-form-field'


class RenderedForm(RenderedElement):
    @property
    def children(self):
        if self._element.context_var_name:
            form_obj = self._context[self._element.context_var_name]

            for name, field in form_obj.fields.items():
                bf = form_obj[name]
                xml_attrs = {
                    (None, 'name'): name,
                    (None, 'boundField'): bf,
                    (None, 'formReactContextRef'): self._element.xml_attrs['reactContextRef'],
                    (None, 'label-width'): self._element.xml_attrs['label-width'],
                    (None, 'field-width'): self._element.xml_attrs['field-width']
                }
                kr_field = KrField(xml_tag=KrField.TAG_NAME, xml_attrs=xml_attrs)
                yield RenderedField(kr_field, self._context)

        for child in super().children:
            yield child


class KrForm(BaseElement):
    RENDERED_ELEMENT_CLASS = RenderedForm

    def _parse_xml_attrs(self, xml_attrs):
        attrs = super()._parse_xml_attrs(xml_attrs)

        form_obj = attrs.pop(f'{{{XML_NAMESPACE_DATA_BINDING}}}object', None)
        if form_obj is None:
            var_name = None
        else:
            var_name = form_obj.expr

        if 'method' not in attrs.keys():
            attrs['method'] = 'POST'

        if f'{{{XML_NAMESPACE_DATA_BINDING}}}csrfmiddlewaretoken' not in attrs.keys():
            attrs[f'{{{XML_NAMESPACE_DATA_BINDING}}}csrfmiddlewaretoken'] = Bind(expr='djsamon.csrf_token')

        if 'reactContextRef' not in attrs.keys():
            attrs['reactContextRef'] = var_name

        if 'onSubmit' not in attrs.keys():
            attrs['onSubmit'] = f"{attrs['reactContextRef']}.handleSubmit"

        self.context_var_name = var_name
        return attrs

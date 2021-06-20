import enum
import typing as tp
import typesystem as ts
from markupsafe import Markup
from essencia_core.models.abstract import StrEnum



class FieldSet:

    class Person(ts.Schema):
        fullname = ts.String(title='Nome Completo')

        class Gender(StrEnum):
            Male = 'Masculino'
            Female = 'Feminino'

        gender = ts.Choice(choices=Gender, title='Gênero')
        birthdate = ts.Date(title='Data de Nascimento')

    class Address(ts.Schema):
        street = ts.String(title='Logradouro')
        house = ts.String(title='Número/Casa/Lote/Quadra')
        complement = ts.String(title='Complemento')
        neiborhood = ts.String(title='Bairro')
        city = ts.String(title='Cidade')

    class Message(ts.Schema):
        message = ts.Text(title='Mensagem')


class Form:
    engine = ts.forms.Jinja2Forms(package='bootstrap4')
    def __init__(self, schema: ts.Schema, values={}, errors: tp.Mapping = {}):
        self.schema = schema
        self.values = values
        self.errors = errors


    def add(self, v):
        assert isinstance(v, ts.Schema), 'o valor de "v" deve uma classe to tipo Typesystem.Schema'


    @property
    def fields(self):
        return Markup(self.engine.Form(self.schema, values=self.values, errors=self.errors).render_fields())



if __name__ == '__main__':
    data = [
        dict(name='Daniel', key='kkhdhf'),
        dict(fullname='Teste', key='kkhdhf'),
        dict(fullname='OUtro', key='kkhdhf'),
        dict(fullname='Lelia', key='kkhdhf'),
        dict(fullname='Ewerton', key='kkhdhf'),
        dict(fullname='Daniel', key='kkhdhf'),

    ]

    print(make_select('patient', 'Paciente', data=data))
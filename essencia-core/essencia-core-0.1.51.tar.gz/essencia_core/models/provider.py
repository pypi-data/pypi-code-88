import typesystem as ts

from essencia_core.models.abstract import StrEnum, Profile

class Provider(Profile):
    class Profession(StrEnum):
        Medicine = 'Medicina'
        Psychology = 'Psicologia'
        Physiotherapy = 'Fisioterapia'
        Nurse = 'Enfermagem'
    profession = ts.Choice(choices=Profession)
    licence = ts.String(title='Registro Profissional')
    graduation = ts.Integer(title='Ano de Graduação')

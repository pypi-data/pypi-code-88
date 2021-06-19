import typesystem as ts
from essencia.core.models.abstract import Profile, StrEnum

class Provider(Profile):
    class Profession(StrEnum):
        Medicine = 'Medicina'
        Psychology = 'Psicologia'
        Physiotherapy = 'Fisioterapia'
        Nurse = 'Enfermagem'
    profession = ts.Choice(choices=Profession)
    licence = ts.String(title='Registro Profissional')
    graduation = ts.Integer(title='Ano de Graduação')

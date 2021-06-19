import datetime
import typesystem as ts
from .abstract import StrEnum


### SEARCH MODELS

class VisitInfoAndKey(ts.Schema):
    key = ts.String()
    date = ts.Date(title='Data da Visita')
    class VisitType(StrEnum):
        Initial = 'Inicial'
        NewVisit = 'Nova Consulta'
        Revist = 'Retorno'
        Session = 'Sessão'
    #type = ts.Choice(choices=VisitType, title='Tipo de Visita')
    patient_key = ts.String()
    provider_key = ts.String()
    model = ts.String()


    def __gt__(self, other):
        return (self.date) > (other.date)


class PersonKeyFullname(ts.Schema):
    key = ts.String()
    fullname = ts.String()

class ProfileSearch(ts.Schema):
    name = ts.String(min_length=3, title='Nome', description='pelo menos 3 letras')

class ProfileType(ts.Schema):
    class Options(StrEnum):
        Provider = 'Profissional'
        Assistant = 'Assistente'
        Patient = 'Patient'
    profile_type = ts.Choice(choices=Options)

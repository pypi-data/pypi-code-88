import typesystem as ts
from essencia.core.models.abstract import Profile, StrEnum

class Assistant(Profile):
    class AssistantCategory(StrEnum):
        Employee = 'Funcionário'
        Studant = 'Estudante'
        Intern = 'Estagiário'
    category = ts.Choice(choices=AssistantCategory, title='Tipo de Assistente')
    salary = ts.Number(minimum=0, maximum=1500, title='Salário Mensal')
    identity = ts.String(title='Identidade', description='Registro e Número')

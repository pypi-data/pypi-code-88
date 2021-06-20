import datetime as dt
import typesystem as ts
import decimal as dc
from essencia_core.models import abstract


class Service(abstract.BaseModel):
    relation = ts.Object(properties={
        'patient': ts.Object(properties={
            'key': ts.String(),
            'fullname': ts.String(allow_null=True),
            'gender': ts.String(allow_null=True),
            'birthdate': ts.Date(allow_null=True),
        }),
        'provider': ts.Object(properties={
            'key': ts.String(),
        }),
        'date': ts.Date(),
        'financial': ts.Object(properties={
            'value': ts.Decimal(allow_null=True),
            'payment': ts.Object(properties={
                'date': ts.Date(allow_blank=True),
                'value': ts.Decimal(allow_null=True, default=dc.Decimal('0.00')),
                'closed': ts.Boolean(default=False),
                'type': ts.String(),
            }),
        }),
    })
    data = ts.Object(properties={
        'subjective': ts.Text(allow_blank=True),
        'objective': ts.Text(allow_blank=True),
        'assessment': ts.Text(allow_blank=True),
        'plan': ts.Object(properties={
            'instructions': ts.Text(allow_blank=True),
            'prescriptions': ts.Text(allow_blank=True),
            'exam_recipes': ts.Text(allow_blank=True),
            'next_visit': ts.Integer(allow_null=True),
        }),
    })


class VisitFull(abstract.BaseModel):
    patient_key = ts.String()
    provider_key = ts.String()
    main_complaint = ts.Text(title='Queixa Principal', allow_blank=True)
    subjective = ts.Text(title='Descrição dos Sintomas', allow_blank=True)
    objective = ts.Text(title='Descrição dos Sinais', allow_blank=True)
    assessment = ts.Text(title='Avaliação', allow_blank=True)
    plan = ts.Text(title='Plano Terapêutico', allow_blank=True)
    exam_recipe = ts.Text(title='Solicitação de Exames', allow_blank=True)
    prescription = ts.Text(title='Prescrição', allow_blank=True)
    next_visit_date = ts.Date(allow_blank=True)
    next_visit_time = ts.Time(allow_blank=True)


class Pharmacotherapy(abstract.BaseModel):
    medication = ts.String()
    posology = ts.String(allow_blank=True)
    pro = ts.String(allow_blank=True)
    con = ts.String(allow_blank=True)


class Treatment(abstract.BaseModel):
    pharmacotherapy = ts.Array(items=[ts.Reference(to='Pharmacotherapy')], allow_null=True)
    psychotherapy = ts.Text(allow_blank=True)


class Objective(abstract.BaseModel):
    mental = ts.Text(title='Exame Mental', allow_blank=True)
    physical = ts.Text(title='Exame Físico', allow_blank=True)


class PatientProfessionalRelation(abstract.BaseModel):
    patient_key = ts.String(title='Id do Paciente')
    provider_key = ts.String(title='Id do Profissional')
    date = ts.Date(title='Data', allow_null=True)

    def __str__(self):
        if not hasattr(self, 'date'):
            setattr(self, 'date', dt.date.today())
        return '{}_{}_{}'.join([str(self.date).replace('-',''), self.patient_key, self.provider_key])

    class Date(ts.Schema):
        date = ts.Date(title='Data')







class ClinicalNote(abstract.BaseModel):

    class SubjectiveNote(abstract.BaseModel):
        complaints = ts.Text(title='Queixa Principal', allow_blank=True)
        symptoms = ts.Text(title='Sintomas Atuais', allow_blank=True)
        medication = ts.Text(title='Medicações Atuais', allow_blank=True)
        context = ts.Text(title='Contexto Relacionado', allow_blank=True)

    class ObjectiveNote(abstract.BaseModel):
        mental = ts.Text(title='Exame Mental', allow_blank=True)
        physical = ts.Text(title='Exame Físico', allow_blank=True)

    class Vitals(abstract.BaseModel):
        weight = ts.Float(minimum=0, maximum=250, description='Kg', allow_null=True)
        heigth = ts.Float(minimum=0, maximum=210, allow_null=True)
        hr = ts.Integer(minimum=0, maximum=300, description='batimentos por minuto', allow_null=True)
        bp = ts.String(title='pressão sanguínea', description='mmHg', allow_blank=True)




class Visit(abstract.BaseModel):
    patient_key = ts.String(title='Id do Paciente')
    provider_key = ts.String(title='Id do Profissional')


    class SubjectiveNotes(abstract.BaseModel):
        complaints = ts.Text(title='Queixa Principal', allow_blank=True)
        symptoms = ts.Text(title='Sintomas Atuais', allow_blank=True)
        medication = ts.Text(title='Medicações Atuais', allow_blank=True)
        context = ts.Text(title='Contexto Relacionado', allow_blank=True)



class Episode(abstract.BaseModel):
    patient_key = ts.String(title='Paciente', description='patient_key')
    owner = ts.String(allow_blank=True, title='Proprietário')
    subjective = ts.Text(allow_blank=True, title='Dados subjetivos')
    context = ts.Text(allow_blank=True, title='Contexto do episódio')
    objective = ts.Text(allow_blank=True, title='Dados objetivos')
    complement = ts.Text(allow_blank=True, title='Informações complementares')
    date = ts.Date(allow_null=True, title='Data do episódio')
    age = ts.Float(allow_null=True, title='Idade no episódio')



    class Input(abstract.BaseModel):
        subjective = ts.Text(allow_blank=True, title='Dados subjetivos')
        context = ts.Text(allow_blank=True, title='Contexto do episódio')
        objective = ts.Text(allow_blank=True, title='Dados objetivos')
        complement = ts.Text(allow_blank=True, title='Informações complementares')
        date = ts.Date(allow_null=True, title='Data do episódio')
        age = ts.Float(allow_null=True, title='Idade no episódio')

    class Visit(abstract.BaseModel):
        subjective = ts.Text(allow_blank=True, title='Dados subjetivos')
        context = ts.Text(allow_blank=True, title='Contexto do episódio')
        objective = ts.Text(allow_blank=True, title='Dados objetivos')
        complement = ts.Text(allow_blank=True, title='Informações complementares')
        assessment = ts.Text(allow_blank=True, title='Avaliação')
        plan = ts.Text(allow_blank=True, title='Plano Terapêutico')
        prescription = ts.Text(allow_blank=True, title='Prescrição')
        exam_recipe = ts.Text(allow_blank=True, title='Solicitação de exames')
        next_visit = ts.Date(allow_blank=True, title='Próxima Consulta')



class ClinicalRecord(abstract.BaseModel):
    patient_key = ts.String()
    provider_key = ts.String()
    subjective = ts.Text(allow_blank=True, title='Dados subjetivos')
    context = ts.Text(allow_blank=True, title='Contexto do episódio')
    weight = ts.Float(minimum=0, maximum=250, description='Kg', allow_null=True)
    hr = ts.Integer(minimum=0, maximum=300, description='batimentos por minuto', allow_null=True)
    bp = ts.String(title='pressão sanguínea', description='mmHg', allow_blank=True)
    mental = ts.Text(title='Exame Mental', allow_blank=True)
    physical = ts.Text(title='Exame Físico', allow_blank=True)
    complement = ts.Text(allow_blank=True, title='Informações complementares')
    assessment = ts.Text(allow_blank=True, title='Avaliação')
    plan = ts.Text(allow_blank=True, title='Plano Terapêutico')
    prescription = ts.Text(allow_blank=True, title='Prescrição')
    exam_recipe = ts.Text(allow_blank=True, title='Solicitação de exames')
    next_visit_days = ts.Integer(allow_null=True, title='Dias para próxima visita')

    class Visit(abstract.BaseModel):
        subjective = ts.Text(allow_blank=True, title='Dados subjetivos')
        context = ts.Text(allow_blank=True, title='Contexto do episódio')
        weight = ts.Float(minimum=0, maximum=250, description='Kg', allow_null=True)
        hr = ts.Integer(minimum=0, maximum=300, description='batimentos por minuto', allow_null=True)
        bp = ts.String(title='pressão sanguínea', description='mmHg', allow_blank=True)
        mental = ts.Text(title='Exame Mental', allow_blank=True)
        physical = ts.Text(title='Exame Físico', allow_blank=True)
        complement = ts.Text(allow_blank=True, title='Informações complementares')
        assessment = ts.Text(allow_blank=True, title='Avaliação')
        plan = ts.Text(allow_blank=True, title='Plano Terapêutico')
        prescription = ts.Text(allow_blank=True, title='Prescrição')
        exam_recipe = ts.Text(allow_blank=True, title='Solicitação de exames')
        next_visit_days = ts.Integer(allow_null=True, title='Dias para próxima visita')


class VisitBase(ts.Schema):
    relation = ts.Object(properties={
        'patient': ts.Object(properties={
            'key': ts.String(),
            'fullname': ts.String(),
        }),
        'provider': ts.Object(properties={
            'key': ts.String(),
            'fullname': ts.String(),
        })
    })
    object = ts.Object(properties={
        'date': ts.Date(default=dt.date.today()),
        'model': ts.String(allow_blank=True),
        'code': ts.String(allow_blank=True)
    })
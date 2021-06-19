from marshmallow import Schema, fields, validate
import sqlalchemy as sa
from flama.applications import Flama
from flama.resources import CRUDListResource
from essencia_pack.deta_api import connect
import uvicorn


class PatientSchema(Schema):
    key = fields.String()
    fullname = fields.String()
    birthdate = fields.String()
    gender = fields.String()


metadata = sa.MetaData()

PatientModel = sa.Table(
    'patient',
    metadata,
    sa.Column('key', sa.String, primary_key=True),
    sa.Column('fullname', sa.String),
    sa.Column('birthdate', sa.String),
    sa.Column('gender', sa.String),
)


async def get_patients():
    conn = await connect('Patient')
    result = next(conn.fetch({}))
    return result

async def save_patient(patient: PatientSchema):
    conn = await connect('Patient')
    result = conn.put(patient)
    return result

app = Flama(
    components=[],      # Without custom components
    title="First Flama",        # API title
    version="0.1",      # API version
    description="Alternative web using starlette",  # API description
    schema="/schema/",  # Path to expose OpenAPI schema
    docs="/docs/",      # Path to expose Swagger UI docs
    redoc="/redoc/",    # Path to expose ReDoc docs
)


# Views
async def list_patients(name: str = None) -> Patient(many=True):
    """
    description:
        List the patients registered. There is an optional query parameter that
        specifies a name for filtering the collection based on it.
    responses:
        200:
            description: List patients.
    """
    return [ patient for patient in await get_patients() if name in (patient[ "fullname" ], None) ]


async def create_patient(patient: Patient) -> Patient:
    """
    description:
        Create a new puppy using data validated from request body and add it
        to the collection.
    responses:
        200:
            description: Puppy created successfully.
    """
    return await save_patient(patient)


app.add_route("/patients/", list_patients, methods=["GET"])
app.add_route("/patients/", create_patient, methods=["POST"])

if __name__ == '__main__':
    uvicorn.run('patient:app', host='0.0.0.0', port=8000, reload=True)
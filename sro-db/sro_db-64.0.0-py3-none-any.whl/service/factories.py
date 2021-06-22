from sro_db.service.stakeholder.service import *
from sro_db.service.relationship.service import *

import factory

# stakeholders
class PersonFactory(factory.Factory):
    class Meta:
        model = PersonService

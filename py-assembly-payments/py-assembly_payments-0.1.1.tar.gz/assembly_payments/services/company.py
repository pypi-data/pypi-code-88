
from assembly_payments.services.base import BaseService
from assembly_payments.types import Company, CompanyRequest


class CompanyService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endpoint = "/companies"

    def list(self, *args, **kwargs):
        response = self._execute(CompanyService.GET, self.endpoint)
        return [Company(**company) for company in response.get('companies', [])]

    def create(self, **kwargs):
        data = CompanyRequest(**kwargs)
        response = self._execute(CompanyService.POST, self.endpoint, data=data.dict())
        return Company(**response['companies'])

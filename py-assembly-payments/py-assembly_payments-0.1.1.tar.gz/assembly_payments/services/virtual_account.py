
from assembly_payments.services.base import BaseService
from assembly_payments.types import VirtualAccount, VirtualAccountRequest


class VirtualAccountService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endpoint = "/virtual_accounts"

    def get(self, virtual_account_id):
        response = self._execute(VirtualAccountService.GET, f"{self.endpoint}/{virtual_account_id}", url=self.virtual_accounts_url)
        return VirtualAccount(**response)

    def create(self, *args, **kwargs):
        data = VirtualAccountRequest(**kwargs).dict()
        wallet_account_id = data.pop("wallet_account_id")
        response = self._execute(VirtualAccountService.POST, f"/wallet_accounts/{wallet_account_id}/virtual_accounts", data=data, url=self.virtual_accounts_url)
        return VirtualAccount(**response)

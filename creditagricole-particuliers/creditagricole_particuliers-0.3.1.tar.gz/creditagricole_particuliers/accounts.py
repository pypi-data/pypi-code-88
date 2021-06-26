
import requests
import json

class Accounts:
    def __init__(self, session):
        """operations class"""
        self.session = session
        self.list = []
        
        self.get_accounts()
        
    def __iter__(self):
        """iter"""
        self.n = 0
        return self
        
    def __next__(self):
        """next"""
        if self.n < len(self.list):
            op = self.list[self.n]
            self.n += 1
            return op
        else:
            raise StopIteration
            
    def get_accounts(self):
        """get accounts"""
        # call operations ressources
        url = "%s" % self.session.url
        url += "/ca-%s/particulier/operations/" % self.session.region
        url += "moyens-paiement/virement/jcr:content.accounts.json"
        r = requests.get(url=url,
                         verify=self.session.ssl_verify,
                         cookies=self.session.cookies)
        if r.status_code != 200:
            raise Exception( "[error] get accounts: %s - %s" % (r.status_code, r.text) )
           
        # success
        accounts_number = []
        for account in json.loads(r.text):
            if "accountNumber" in account:
                if account["accountNumber"] in accounts_number:
                    continue
                accounts_number.append(account["accountNumber"])   
                account["balanceValue"] = account["balanceValue"] / 100
                self.list.append(account)

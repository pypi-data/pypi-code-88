
import requests
import json
from datetime import datetime, timedelta

from creditagricole_particuliers import operations

FAMILLE_PRODUITS = [
     {"code": 1, "familleProduit": "COMPTES"}, 
     {"code": 3, "familleProduit": "EPARGNE_DISPONIBLE"}, 
     {"code": 7, "familleProduit": "EPARGNE_AUTRE"},
]

class Account:
    def __init__(self, session, descr):
        """account class"""
        self.session = session
        self.descr = descr
        self.numeroCompte = descr["numeroCompte"]
        self.compteIdx = descr["index"]
        self.grandeFamilleCode = descr["grandeFamilleProduitCode"]

    def __str__(self):
        """str"""
        return f"Compte[numero={self.numeroCompte}, produit={self.descr['libelleProduit']}]"
 
    def get_operations(self, date_start=None, date_stop=None, count=100):
        """get operations"""
        if date_stop is None:
            current_date = datetime.today()
            previous_date = current_date - timedelta(days=30)
            date_stop = current_date.strftime('%Y-%m-%d')
            date_start = previous_date.strftime('%Y-%m-%d')
        return operations.Operations(session=self.session, compteIdx=self.compteIdx, grandeFamilleCode=self.grandeFamilleCode,
                          date_start=date_start, date_stop=date_stop, count=count)

    def as_json(self):
        """return as json"""
        return json.dumps(self.descr)

    def get_solde(self):
        """get solde"""
        if "montantEpargne" in self.descr:
            return self.descr["montantEpargne"]
        return self.descr["solde"]

class Accounts:
    def __init__(self, session):
        """operations class"""
        self.session = session
        self.list = []
        
        self.get_accounts_per_products()

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

    def search(self, num):
        """search account according to the num"""
        for acc in self.list:
            if acc.numeroCompte == num:
                return acc
        raise Exception( "[error] account not found" )

    def as_json(self):
        """as json"""
        _accs = []
        for acc in self.list:
            _accs.append(acc.descr)
        return json.dumps(_accs)

    def get_accounts_per_products(self):
        """get accounts per products"""
        for f in FAMILLE_PRODUITS:
            # call operations ressources
            url = "%s" % self.session.url
            url += "/ca-%s/particulier/operations/" % self.session.region
            url += "synthese/jcr:content.produits-valorisation.json/%s" % f["code"]
            r = requests.get(url=url,
                            verify=self.session.ssl_verify,
                            cookies=self.session.cookies)
            if r.status_code != 200:
                raise Exception( "[error] get accounts: %s - %s" % (r.status_code, r.text) )

            for descr in json.loads(r.text):
                self.list.append( Account(self.session, descr) )

    def get_solde(self):
        """get global solde"""
        solde = 0
        for acc in self.list:
            solde += acc.get_solde()
        return round(solde, 2)
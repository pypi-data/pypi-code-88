from creditagricole_particuliers import Authenticator, Accounts

# Définition du compte courant et du mot de passe
username = "<n° de compte bancaire>"
password = [1, 2, 3, 4, 5, 6]

# Authentification du client 
session = Authenticator(username=username,
                        password=password)
                        
# Récupération de l'ensemble des comptes
accounts = Accounts(session=session)

# Affichage du résultat
print(accounts.list)
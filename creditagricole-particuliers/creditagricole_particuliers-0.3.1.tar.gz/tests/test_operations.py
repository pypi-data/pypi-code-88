from creditagricole_particuliers import Authenticator, Operations

# Définition du compte courant et du mot de passe
username = "<n° de compte bancaire>"
password = [1, 2, 3, 4, 5, 6]

# Définition de la date de début et fin à récupérer
date_start = "2020-02-21"
date_stop = "2020-02-21"

# Authentification du client 
session = Authenticator(username=username,
                        password=password)

# Récupération des opérations en fonction de la date
operations = Operations(session=session,
                        date_start=date_start,
                        date_stop=date_stop)

# Affichage du résultat
print(operations.list)
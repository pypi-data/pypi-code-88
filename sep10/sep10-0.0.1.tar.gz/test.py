from Authenticator.sep10 import Sep10

from pathlib import Path


secret = Path(".secrets").read_text()




webauth = Sep10("TZS", "GA2MSSZKJOU6RNL3EJKH3S5TB5CDYTFQFWRYFGUJVIN5I6AOIRTLUHTO", secret)

print(webauth.run_auth())
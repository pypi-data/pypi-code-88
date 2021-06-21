from kubehelm.models.scripts import RunAppScript
from kubehelm.models.manifest import Manifest


class Ingress(RunAppScript):
    script_name = "ingress.bash"
    allowed_methods = ["install", "update"]


class Cert(RunAppScript):
    script_name = "cert_manager.bash"
    allowed_methods = ["install", "update"]


class Issuerstaging(RunAppScript):
    script_name = 'letsencrypt_staging.bash'
    allowed_methods = ["install", "update"]


class Issuerproduction(RunAppScript):
    script_name = 'letsencrypt_production.bash'
    allowed_methods = ["install", "update"]

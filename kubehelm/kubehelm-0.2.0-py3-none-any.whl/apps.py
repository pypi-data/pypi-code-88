from kubehelm.script import RunAppScript
from kubehelm.models.manifest import Manifest
from kubehelm.models.helm import Helm


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


class Django(Manifest):
    template_name = 'manifests/django.yaml'
    required_context = ["namespace", "app_name", "image_name", "image_tag"]
    default_context = {
        "manifest_name": "Django",
        "namespace": "default",
        "image_name": "asim3/django",
        "image_tag": "latest",
        "memory_limit": "128Mi",
        "cpu_limit": "50m",
        "secrets": [],
    }


class Whoami(Manifest):
    template_name = 'manifests/whoami.yaml'
    required_context = ["namespace", "app_name"]
    default_context = {
        "manifest_name": "Whoami",
        "namespace": "default",
        "image_name": "asim3/whoami",
        "image_tag": "1.3",
        "memory_limit": "128Mi",
        "cpu_limit": "50m",
        "secrets": [],
    }


class Mariadb(Helm):
    required_context = ["namespace", "app_name"]
    chart_name = "bitnami/mariadb"


class Phpmyadmin(Helm):
    required_context = ["namespace", "app_name"]
    chart_name = "bitnami/phpmyadmin"


class Wordpress(Helm):
    required_context = ["namespace", "app_name"]
    chart_name = "bitnami/wordpress"


class Osclass(Helm):
    required_context = ["namespace", "app_name"]
    chart_name = "bitnami/osclass"

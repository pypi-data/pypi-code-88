from k8s.models.helm import Helm


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

import abc


class Forge(abc.ABC):
    @abc.abstractmethod
    def user_get(self, user):
        ...

    @abc.abstractmethod
    def user_create(self, user):
        ...

    @abc.abstractmethod
    def project_get(self, user, namespace, project):
        ...

    @abc.abstractmethod
    def project_delete(self, user, namespace, project):
        ...

    @abc.abstractmethod
    def project_create(self, admin, user, namespace, project, **data):
        ...

    @abc.abstractmethod
    def project_export(self, user, namespace, project, filename):
        ...

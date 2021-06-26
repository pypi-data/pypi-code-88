from .abstract import AbstractInterface


class LanguagesInterface(AbstractInterface):
    create_fields = ['name', 'seccomp_rule_name']
    retrieve_fields = ['id', 'name', 'seccomp_rule_name']
    update_fields = ['name', 'seccomp_rule_name']
    table_name = 'judge.LANGUAGES'

from .abstract import AbstractInterface

class LanguagesInterface(AbstractInterface):
    def __init__(self, cur):
        super().__init__(cur)
        self.create_fields = ['name', 'seccomp_rule_name']
        self.retrieve_fields = ['id', 'name', 'seccomp_rule_name']
        self.update_fields = self.create_fields
        self.table_name = 'judge.LANGUAGES'

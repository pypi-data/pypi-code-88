import json


class Json:

    def get_variable_from_file(self, var_name, file):
        with open(file) as f:
            composer = json.load(f)

        if var_name in composer:
            var_value = composer[var_name]
        else:
            raise Exception('Var name not found.')

        return var_value

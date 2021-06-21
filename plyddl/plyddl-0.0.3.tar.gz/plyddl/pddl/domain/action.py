class Action:

    def __init__(self, name, parameter, precondition, effects):
        self.name = name
        self.parameter = parameter
        self.precondition = precondition
        self.effects = effects

    def update_params(self, param_type, param_mapping, p_objects):
        self.parameter = param_type
        for p in self.precondition:
            p.update_params(param_mapping, p_objects)
        for e in self.effects:
            e.update_params(param_mapping, p_objects)

        return [self.parameter, str(self.precondition)]
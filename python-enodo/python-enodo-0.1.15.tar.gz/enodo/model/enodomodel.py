class EnodoModel:
    __slots__ = ('name', 'model_arguments', 'base_analysis', 'forecast', 'anomaly_detect', 'static_rules')

    def __init__(self, name, model_arguments, base_analysis=False, forecast=False, anomaly_detect=False, static_rules=False):
        """
        :param name:
        :param model_arguments:  in form of  {'name': ..., 'required': True, 'description': ''} 
        """
        self.name = name
        self.model_arguments = model_arguments

        self.base_analysis = base_analysis
        self.forecast = forecast
        self.anomaly_detect = anomaly_detect
        self.static_rules = static_rules

    @classmethod
    def to_dict(cls, model):
        return {
            'name': model.name,
            'model_arguments': model.model_arguments,
            'base_analysis': model.base_analysis,
            'forecast': model.forecast,
            'anomaly_detect': model.anomaly_detect,
            'static_rules': model.static_rules
        }

    @classmethod
    def from_dict(cls, model):
        return EnodoModel(**model)
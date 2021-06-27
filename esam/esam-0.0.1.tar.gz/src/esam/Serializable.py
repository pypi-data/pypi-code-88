import logging
import json
import jsonpickle

class Serializable(json.JSONEncoder):

    def ToJSON(self):
        return jsonpickle.encode(self)

    #This isn't necessary.
    #Problem: How do you know what object to call FromJSON on if the class is defined in the json, which has not yet been read?
    # def FromJSON(self, json):
    #     #TODO: can we make this safer?
    #     self = jsonpickle.decode(jsonEncoding)
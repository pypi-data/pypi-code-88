import json


class Mock(object):

    data = None

    def to_string(self):
        if not isinstance(self.data,
                          (bytes, str, int, float, list, tuple, dict)):
            raise NotImplementedError(
                "to_string should be self defined for data type = {}".format(
                    type(self.data)))
        if isinstance(self.data, bytes):
            return str(self.data, encoding="utf8")
        if isinstance(self.data, (str, int, float)):
            return str(self.data)
        return json.dumps(self.data)

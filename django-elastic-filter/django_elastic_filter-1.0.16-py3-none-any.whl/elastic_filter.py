class ElasticFilter:
    """
    Generate model of our class
    """
    def __init__(self, scope, connector, request):
        self.connector = connector
        self.scope = scope
        self.rest = {}
        self.request = request

    def get_scope_other_fields(self):
        """
        Return fields in a model and other fields that have their own fields.

        :return dic:
        """
        import urllib.parse as p
        query_string = p.parse_qs(self.request.META['QUERY_STRING'])

        fields = query_string[self.scope][0].split(',')
        rest = {}
        for item in query_string:
            if item in fields:
                rest[item] = query_string[item]
                fields.remove(item)

        return {"fields": fields,
                "rest": rest}

import cg_learning_client.CGLearningClient as Client


class CGData:
    def __init__(self):
        self.pageable = True
        self.page = 1
        self.limit = 20
        self.lazyLoad = True
        self.next_page = None
        self.data = None
        self.client = None


class CGXAPIData(CGData):
    def __init__(self, client: Client, response=None, query_params: dict=None):
        super().__init__()
        self.client = client
        self.params = query_params
        self.headers = None
        self.headers_op = None

    def get_available_headers(self):
        if self.headers is not None:
            return self.headers
        self.headers_op = self.client.generate_operator('Query', self.params)
        self.headers = self.client.query_operator_output(self.headers_op['id'])
        return self.headers

    def get_structured_data(self, headers: list=None):
        if self.headers is None:
            tmp = self.get_available_headers()
            if headers is None:
                headers = tmp
            print(self.headers_op['id'])
        operator = self.client.generate_operator('Select', {
            'headers': headers
        }, source=[self.headers_op['id']])
        return self.client.query_operator_output(operator['id'])

class StructuredData(CGData):
    def __init__(self):
        super().__init__()

class Tickets():
    def __init__(self, base_url, make_http_request):
        self.base_url = base_url
        self.make_http_request = make_http_request

    def create(self, data):
        """Create a ticket based on the data passed"""
        endpoint = f'{self.base_url}/tickets'
        response = self.make_http_request('post', endpoint, data)
        return response

    def all(self):
        """Retrieve all tickets"""
        endpoint = f'{self.base_url}/tickets'
        response = self.make_http_request('get', endpoint)
        return response

    def retrieve(self, id):
        """Retrieve a single ticket"""
        endpoint = f'{self.base_url}/tickets/{id}'
        response = self.make_http_request('get', endpoint)
        return response

    def update(self, id, data):
        """Update a ticket with the passed params"""
        endpoint = f'{self.base_url}/tickets/{id}'
        response = self.make_http_request('patch', endpoint, data)
        return response

    def delete(self, id):
        """Delete a ticket with the ID passed"""
        endpoint = f'{self.base_url}/tickets/{id}'
        response = self.make_http_request('delete', endpoint)
        return response

class Locations():
    def __init__(self, base_url, make_http_request):
        self.base_url = base_url
        self.make_http_request = make_http_request

    def create(self, data):
        """Create a location based on the data passed"""
        endpoint = f'{self.base_url}/locations'
        response = self.make_http_request('post', endpoint, data)
        return response

    def all(self):
        """Retrieve all locations"""
        endpoint = f'{self.base_url}/locations'
        response = self.make_http_request('get', endpoint)
        return response

    def retrieve(self, id):
        """Retrieve a single location"""
        endpoint = f'{self.base_url}/locations/{id}'
        response = self.make_http_request('get', endpoint)
        return response

    def update(self, id, data):
        """Update a location with the passed params"""
        endpoint = f'{self.base_url}/locations/{id}'
        response = self.make_http_request('patch', endpoint, data)
        return response

    def delete(self, id):
        """Delete a location with the ID passed"""
        endpoint = f'{self.base_url}/locations/{id}'
        response = self.make_http_request('delete', endpoint)
        return response

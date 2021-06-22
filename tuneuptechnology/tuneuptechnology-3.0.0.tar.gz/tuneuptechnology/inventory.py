class Inventory():
    def __init__(self, base_url, make_http_request):
        self.base_url = base_url
        self.make_http_request = make_http_request

    def create(self, data):
        """Create an inventory item based on the data passed"""
        endpoint = f'{self.base_url}/inventory'
        response = self.make_http_request('post', endpoint, data)
        return response

    def all(self):
        """Retrieve all inventory"""
        endpoint = f'{self.base_url}/inventory'
        response = self.make_http_request('get', endpoint)
        return response

    def retrieve(self, id):
        """Retrieve a single inventory item"""
        endpoint = f'{self.base_url}/inventory/{id}'
        response = self.make_http_request('get', endpoint)
        return response

    def update(self, id, data):
        """Update an inventory item with the passed params"""
        endpoint = f'{self.base_url}/inventory/{id}'
        response = self.make_http_request('patch', endpoint, data)
        return response

    def delete(self, id):
        """Delete an inventory item with the ID passed"""
        endpoint = f'{self.base_url}/inventory/{id}'
        response = self.make_http_request('delete', endpoint)
        return response

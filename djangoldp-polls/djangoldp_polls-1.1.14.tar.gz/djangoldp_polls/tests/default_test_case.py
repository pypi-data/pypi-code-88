from rest_framework.test import APITestCase, APIClient
from djangoldp_polls.tests.models import User


class DefaultTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.setUpLoggedInUser()

    def setUpLoggedInUser(self):
        self.user = User(email='test@mactest.co.uk', first_name='Test', last_name='Mactest', username='test',
                         password='glass onion')
        self.user.save()
        self.client.force_authenticate(user=self.user)

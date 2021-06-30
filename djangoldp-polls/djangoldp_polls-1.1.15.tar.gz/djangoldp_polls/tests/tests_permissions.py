import uuid
import json
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.test import APITestCase, APIClient

from djangoldp_polls.models import Poll, PollOption, Vote
from djangoldp_account.models import LDPUser
from djangoldp_circle.models import Circle, CircleMember

class PermissionsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def buildUser(self, username):
        user = LDPUser(email=username + '@test.startinblox.com', first_name='Test', last_name='Mactest', username=username,
                         password='glass onion')
        user.save()
        return user

    def buildPoll(self, title, circle):
        poll = Poll.objects.create(endDate=datetime.now(), title=title, hostingOrganisation='Test',
                                   shortDescription='Hello', longDescription='Hello World', circle=circle)
        return poll

    def test_list_polls_public(self):
        user1 = self.buildUser('user1')
        self.client.force_authenticate(user1)

        circle = Circle.objects.create(status='Public')

        self.buildPoll('poll1', circle)

        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('poll1', response.data['ldp:contains'][0]['title'])


    def test_list_polls_private_member(self):
        user1 = self.buildUser('user1')
        self.client.force_authenticate(user1)

        circle = Circle.objects.create(status='Private')
        user1Member = CircleMember.objects.create(circle=circle, user=user1)

        self.buildPoll('poll1', circle)

        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('poll1', response.data['ldp:contains'][0]['title'])

    def test_list_polls_private_no_member(self):
        user1 = self.buildUser('user1')
        circle = Circle.objects.create(status='Private', owner=user1)
        self.buildPoll('poll1', circle)

        user2 = self.buildUser('user2')
        self.client.force_authenticate(user2)

        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(0, len(response.data['ldp:contains']))
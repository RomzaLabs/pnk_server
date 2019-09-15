from django.urls import reverse
from django.forms.models import model_to_dict
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from .factories import MissionFactory, user1


class TestMissionListTestCase(APITestCase):
    """
    Tests /missions list operations.
    """

    def setUp(self):
        user1.save()
        self.url = reverse('mission-list')
        self.mission_data = model_to_dict(MissionFactory.build())

    def test_post_request_with_no_token_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_request_with_no_token_succeeds(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

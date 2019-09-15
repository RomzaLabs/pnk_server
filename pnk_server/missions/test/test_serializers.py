from django.test import TestCase
from django.forms.models import model_to_dict
from nose.tools import eq_, ok_

from .factories import MissionFactory, user1
from ..serializers import MissionSerializer


class TestMissionSerializer(TestCase):

    def setUp(self):
        user1.save()
        mission = MissionFactory.build()
        self.mission_data = model_to_dict(mission)

    def test_serializer_with_empty_data(self):
        serializer = MissionSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = MissionSerializer(data=self.mission_data)
        ok_(serializer.is_valid())

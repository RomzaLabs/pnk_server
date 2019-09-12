from rest_framework import serializers
from .models import Mission
from ..users.serializers import UserSerializer


class MissionSerializer(serializers.ModelSerializer):
    commander = UserSerializer()
    rsvp_users = UserSerializer(many=True)
    attended_users = UserSerializer(many=True)

    class Meta:
        model = Mission
        fields = '__all__'

from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Mission
from .serializers import MissionSerializer


class MissionDetailViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    """
    Create, Retrieve, Update, Destroy and List missions
    TODO: Create should only be done by authenticated members.
    TODO: Update should only be done by authenticated members.
    TODO: Destroy should only be done by owner.
    """
    queryset = Mission.objects.all().order_by("-mission_date")
    serializer_class = MissionSerializer
    permission_classes = (AllowAny,)


class MissionListViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
    Create Missions.
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = (AllowAny,)

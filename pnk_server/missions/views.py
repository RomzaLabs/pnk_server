from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Mission
from ..users.permissions import IsUserOrReadOnly
from .serializers import MissionSerializer


class MissionViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    Create, Retrieve, Update, Destroy and List missions
    TODO: Create should only be done by authenticated members.
    TODO: Update should only be done by authenticated members.
    TODO: Destroy should only be done by owner.
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = (AllowAny,)
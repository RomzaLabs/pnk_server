from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser
from django.db.models import Q
from .models import User
from .permissions import IsUserOrReadOnly, IsSuperuserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserDetailViewSet(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.filter(Q(is_superuser=False))
    serializer_class = UserSerializer
    lookup_field = "username"
    permission_classes = (IsUserOrReadOnly,)


class UserListViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.filter(Q(is_superuser=False)).order_by("username")
    serializer_class = CreateUserSerializer
    permission_classes = (IsSuperuserOrReadOnly,)

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework_filters.backends import RestFrameworkFilterBackend

from thirty.profiles.filters import ProfilesFilter
from thirty.profiles.models import Profile
from thirty.profiles.serializers import ProfileSerializer, ProfileSimpleSerializer


class ProfilesViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    filter_backends = (SearchFilter, RestFrameworkFilterBackend, OrderingFilter)
    search_fields = ["name"]
    filterset_class = ProfilesFilter
    ordering = ("name",)

    def get_serializer_class(self):
        if self.action == "list":
            return ProfileSimpleSerializer
        else:
            return ProfileSerializer

from rest_framework_filters import FilterSet

from thirty.profiles.models import Profile


class ProfilesFilter(FilterSet):

    class Meta:
        model = Profile
        fields = [
            "name",
        ]



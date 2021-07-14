from rest_framework_filters import FilterSet

from thirty.profiles.models import Profile


class PostsFilter(FilterSet):

    class Meta:
        model = Profile
        fields = [
            "tittle",
        ]



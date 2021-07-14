from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework_filters.backends import RestFrameworkFilterBackend

from thirty.posts.filters import PostsFilter
from thirty.posts.models import Post
from thirty.posts.serializers import PostSerializer, PostSimpleSerializer


class PostsViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    filter_backends = (SearchFilter, RestFrameworkFilterBackend, OrderingFilter)
    search_fields = ["tittle"]
    filterset_class = PostsFilter
    ordering = ("name",)

    def get_serializer_class(self):
        if self.action == "list":
            return PostSimpleSerializer
        else:
            return PostSerializer

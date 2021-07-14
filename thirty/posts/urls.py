from rest_framework import routers
from django.urls import path, include

from thirty.posts import views

app_name = "posts"

router = routers.SimpleRouter()

router.register(r"posts", views.PostsViewSet, basename="posts")

urlpatterns = [
    path('', include(router.urls)),
]

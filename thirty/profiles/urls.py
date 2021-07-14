from rest_framework import routers
from django.urls import path, include

from thirty.profiles import views

app_name = "profiles"

router = routers.SimpleRouter()

router.register(r"profiles", views.ProfilesViewSet, basename="profiles")

urlpatterns = [
    path('', include(router.urls)),
]

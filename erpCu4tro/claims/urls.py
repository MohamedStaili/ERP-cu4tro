from django.urls import include, path
from rest_framework import routers
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)
from .views import ClientClaimViewSet, AdminClaimViewSet
router = routers.DefaultRouter()
router.register(r"clients/claims", ClientClaimViewSet, basename="clients-claims")
router.register(r"admins/claims", AdminClaimViewSet, basename="admin-claims")
#router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
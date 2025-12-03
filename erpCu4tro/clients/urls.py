from django.urls import include, path
from rest_framework import routers
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)
from .views import ClientViewSet, ClientProductsViewSet
router = routers.DefaultRouter()
router.register(r"admins/clients", ClientViewSet, basename="admin-clients")
router.register(r"admins/clients-products", ClientProductsViewSet, basename="admin-clients-products")
#router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
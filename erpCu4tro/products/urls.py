from django.urls import include, path
from rest_framework import routers
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)
from .views import ProductViews
router = routers.DefaultRouter()
router.register(r"admins/products", ProductViews, basename="admin-products")
#router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
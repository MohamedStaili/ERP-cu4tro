from django.urls import include, path
from rest_framework import routers
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)
from .views import CreateLeadViews
router = routers.DefaultRouter()
router.register(r"admins/leads", CreateLeadViews, basename="admin-leads")
#router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
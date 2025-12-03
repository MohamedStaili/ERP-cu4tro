from django.urls import include, path
from rest_framework import routers
from . import views
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)
from .views import LoginView, RefreshView, MeView, LoogoutView
router = routers.DefaultRouter()
router.register(r"admins/users", views.CreateUserViewSet, basename="admin-user")
#router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    #path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('login/',LoginView.as_view() ),
    path('login/refresh/', RefreshView.as_view()),
    path('account/me/',MeView.as_view()),
    path('logout/',LoogoutView.as_view()),
]
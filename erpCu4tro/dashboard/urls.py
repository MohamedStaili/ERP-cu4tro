from django.urls import path
from .views import AdminDashboardView

urlpatterns = [
    path("admins/dashboard/", AdminDashboardView.as_view(), name="admin-dashboard"),
]

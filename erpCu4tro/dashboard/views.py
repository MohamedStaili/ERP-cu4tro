from django.utils import timezone
from datetime import timedelta

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from accounts.permissions import IsAdmin
from clients.models import Client
from leads.models import Lead
from clients.models import ClientProduct
from claims.models import Claim


class AdminDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get(self, request):

        total_clients = Client.objects.count()
        open_leads = Lead.objects.exclude(workflow_status__in=["converted", "closed"]).count()
        open_orders = ClientProduct.objects.exclude(status__in=["delivered", "canceled"]).count()
        open_claims = Claim.objects.exclude(status__in=["closed", "rejected"]).count()

        
        latest_leads_qs = Lead.objects.select_related("operator", "client").order_by("-id")[:5]
        latest_leads = [
            {
                "id": lead.id,
                "email": lead.email,
                "operator": getattr(lead.operator, "username", None),
                "status": lead.workflow_status,
            
            }
            for lead in latest_leads_qs
        ]

        
        latest_orders_qs = (
            ClientProduct.objects
            .select_related("client", "product", "operator")
            .order_by("-created_at")[:5]
        )
        latest_orders = [
            {
                "id": cp.id,
                "client": str(cp.client),
                "product": str(cp.product),
                "status": cp.status,
                "created_at": cp.created_at.isoformat(),
                "operator": getattr(cp.operator, "username", None),
            }
            for cp in latest_orders_qs
        ]

        
        latest_claims_qs = (
            Claim.objects
            .select_related("client", "operator")
            .order_by("-id")[:5]
        )
        latest_claims = [
            {
                "id": claim.id,
                "client": str(claim.client),
                "status": claim.status,
                "operator": getattr(claim.operator, "username", None),
            
            }
            for claim in latest_claims_qs
        ]

        data = {
            "kpis": {
                "total_clients": total_clients,
                "open_leads": open_leads,
                "open_orders": open_orders,
                "open_claims": open_claims,
            },
            "latest_leads": latest_leads,
            "latest_orders": latest_orders,
            "latest_claims": latest_claims,
        }
        return Response(data, status=status.HTTP_200_OK)

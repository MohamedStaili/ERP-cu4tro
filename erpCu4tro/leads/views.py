from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from accounts.permissions import IsAdmin
from .serializers import LeadSerializer
from .models import Lead
from clients.serializers import ClientSerializer

class CreateLeadViews(viewsets.ModelViewSet):
    queryset= Lead.objects.all().order_by('-id')
    serializer_class= LeadSerializer
    permission_classes = [IsAdmin]

    @action(detail=True, methods=["patch"], url_path="convert-to-client")
    def convert_to_client(self, request, pk=None):
        lead = self.get_object()

        if lead.workflow_status not in ["qualified", "assigned", "contacted"]:
            return Response(
                {"detail": "Ce lead ne peut pas être converti dans ce statut."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        password = request.data.get("password")
        username = request.data.get("username")
        if not password:
            return Response(
                {"detail": "Le mot de passe est obligatoire pour la conversion."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not username:
            return Response(
                {"detail": "Le username est obligatoire pour la conversion."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        client = lead.convert_to_client(password=password,username=username)

        data = ClientSerializer(client).data
        return Response(
            {"lead_id": lead.id, "client": data},
            status=status.HTTP_201_CREATED,
        )

    
  


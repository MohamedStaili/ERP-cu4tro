from rest_framework import viewsets, permissions
from accounts.permissions import IsClient, IsAdmin
from .models import Claim
from .serializers import ClaimSerializer

class ClientClaimViewSet(viewsets.ModelViewSet):
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]

    def get_queryset(self):
        return Claim.objects.filter(client__user=self.request.user)

    def perform_create(self, serializer):
        client = self.request.user.client  
        serializer.save(client=client, status="new")

class AdminClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all().order_by("-id")
    serializer_class = ClaimSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
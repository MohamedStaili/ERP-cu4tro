from django.contrib.auth.models import User, Group
from rest_framework import viewsets,permissions, status 
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, GroupSerializer
from .permissions import IsAdmin
class CreateUserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all().order_by('-date_joined')
    serializer_class= UserSerializer
    permission_classes = [IsAdmin]
    #pas de delete , faire desactiver le compte
    http_method_names=['get', 'post', 'put', 'patch']

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

    def perform_update(self, serializer):
        instance = serializer.save()
        if 'password' in serializer.validated_data:
            instance.set_password(instance.password)
            instance.save()
    
    def perform_destroy(self, instance):
        instance.is_active= False
        instance.save()

class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"detail": "Invalid credentials"},
                status=status.HTTP_404_NOT_FOUND,
            )
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        
        response = Response(
            {
                "message": "User logged successfully",
                "user": {
                    "username": user.username,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )

        #les cookies

        response.set_cookie(
            key="access_token",
            value=access,
            httponly=True,
            secure=False,
            samesite="Lax"
        )

        response.set_cookie(
            key="refresh_token",
            value=refresh,
            httponly=True,
            secure=False,
            samesite="Lax"
        )

        return response

class LoogoutView(APIView):

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")
        if refresh_token:
            try:
                token= RefreshToken(refresh_token)
                token.blacklist()
            except:
                pass
        response = Response(
            {"message": "loggout"},
            status=status.HTTP_200_OK
            )
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
    

class RefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({"detail": "No refresh token"}, status=400)

        try:
            refresh = RefreshToken(refresh_token)
            access = str(refresh.access_token)

            response = Response({"message": "Token refreshed"})
            response.set_cookie(
                "access_token",
                access,
                httponly=True,
                secure=False,
                samesite="Lax"
            )
            return response
        except:
            return Response({"detail": "Invalid token"}, status=400)



class MeView(APIView):
    permission_classes= [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first Name": user.first_name,
            "last Name": user.last_name,
            "roles": list(user.groups.values_list("name", flat=True)),
        })
    



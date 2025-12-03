from rest_framework_simplejwt.authentication import JWTAuthentication
class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
    
        header = self.get_header(request)
        if header is not None:
            return super().authenticate(request)

        cookie_token = request.COOKIES.get("access_token")

        if cookie_token:
            try:
                validated_token = self.get_validated_token(cookie_token)
                user = self.get_user(validated_token)
                return (user, validated_token)  
            except Exception:
                return None

        return None

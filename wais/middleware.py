import jwt
from django.http import JsonResponse
from django.conf import settings

class ClerkAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]  # Extract the token
            try:
                decoded = jwt.decode(token, settings.CLERK_JWT_KEY, algorithms=["RS256"])
                request.user = decoded  # Attach the decoded user info to the request
            except jwt.ExpiredSignatureError:
                return JsonResponse({"error": "Token expired"}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({"error": "Invalid token"}, status=401)

        return self.get_response(request)

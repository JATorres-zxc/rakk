from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import jwt
import os

# Clerk JWT Secret Key (from .env or settings)
CLERK_JWT_KEY = os.getenv("CLERK_JWT_KEY", "your-clerk-secret-key")


@csrf_exempt  # Since it's an API, CSRF protection isn't needed
def protected_view(request):
    # Get Authorization Header
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"error": "Unauthorized - No Token Provided"}, status=401)

    token = auth_header.split(" ")[1]  # Extract token

    try:
        # Decode JWT using Clerk Secret Key
        decoded_token = jwt.decode(token, CLERK_JWT_KEY, algorithms=["RS256"])
        user_email = decoded_token.get("sub")  # Clerk stores user ID in `sub`

        return JsonResponse({"message": f"Hello {user_email}"})  # Return user info

    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "Unauthorized - Token Expired"}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({"error": "Unauthorized - Invalid Token"}, status=401)

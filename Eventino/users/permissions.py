from rest_framework.exceptions import AuthenticationFailed
import jwt


class IsAuthedUser:
    """
    Allows access only to authenticated users
    """

    def has_permission(self, request, view) -> bool:
        if not (token := request.COOKIES.get("jwt")):
            raise AuthenticationFailed("Unauthenticated!")
        try:
            payload = jwt.decode(token, "secret", algorithms="HS256")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")
        return True

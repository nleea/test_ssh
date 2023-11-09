"""
File in which we have the middleware for Django for Authenticating API requests
"""
import json
import logging
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.exceptions import (
    InvalidToken,
    AuthenticationFailed,
    TokenBackendError,
    TokenError,
    exceptions,
)
from django.contrib.auth import get_user_model
from pathlib import Path
import os
import re

User = get_user_model()

# Initialize logger
logger = logging.getLogger(__name__)
# Get JWT secret key

SECRET_KEY = os.environ.get("SECRET_OR_KEY")


class CustomMiddleware(MiddlewareMixin):

    """
    Custom Middleware Class to process a request before it reached the endpoint
    """

    def process_request(self, request):
        """
        Custom middleware handler to check authentication for a user with JWT authentication
        :param request: Request header containing authorization tokens
        :type request: Django Request Object
        :return: HTTP Response if authorization fails, else None
        """
        routes_free = [
            "/api/auth/signin/",
            "/auth/signup/",
            "/admin/",
            "/__debug__/",
            "webhook"
        ]

        match = re.search("|".join(routes_free), request.path)
        if match:
            return None

        jwt_token: str = request.headers.get("authorization", None)
        logger.info(f"request received for endpoint {str(request.path)}")

        content_type = "application/json"

        # If token Exists
        if jwt_token:
            try:
                tokenUser, _ = JWTAuthentication.authenticate(
                    JWTAuthentication(), request
                )
                user = tokenUser

                if not tokenUser.is_authenticated:
                    return HttpResponse(
                        json.dumps({"message": "User not in session"}),
                        content_type=content_type,
                        status=401,
                    )

                if not user:
                    return HttpResponse({"message": "User not found"}, status=401)

                request.user = tokenUser
                return None
            except (
                InvalidToken,
                AuthenticationFailed,
                TokenBackendError,
                TokenError,
                exceptions.ValidationError,
                exceptions.APIException,
                exceptions.PermissionDenied,
            ):
                return HttpResponse(
                    json.dumps(
                        {"message": "Authorization has failed, Please send valid token"}
                    ),
                    content_type=content_type,
                    status=401,
                )
            except Exception as e:
                return HttpResponse(e.args, status=400)
        else:
            return HttpResponse(
                json.dumps(
                    {"message": "Authorization has failed, Please send valid token"}
                ),
                content_type=content_type,
                status=401,
            )

    def process_response(self, request, response):
        return response

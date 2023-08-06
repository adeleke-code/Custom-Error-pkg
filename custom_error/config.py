from rest_framework import status
from .handler import http_error_handler



def created(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Created."

        ctx = {
            "status_code": status.HTTP_201_CREATED,
            "message": message,
            "default_code": "created",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_201_CREATED)

def accepted(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Accepted."

        ctx = {
            "status_code": status.HTTP_202_ACCEPTED,
            "message": message,
            "default_code": "accepted",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_202_ACCEPTED)

def no_content(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "No Content."

        ctx = {
            "status_code": status.HTTP_204_NO_CONTENT,
            "message": message,
            "default_code": "no_content",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_204_NO_CONTENT)

def ok(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "OK."

        ctx = {
            "status_code": status.HTTP_200_OK,
            "message": message,
            "default_code": "ok",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_200_OK)

def success(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Success."

        ctx = {
            "status_code": status.HTTP_200_OK,
            "message": message,
            "default_code": "success",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_200_OK)

def validation_error(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Invalid input."

        ctx = {
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": message,
            "default_code": "invalid",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_400_BAD_REQUEST)


def not_found(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Not found."

        ctx = {
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": message,
            "default_code": "not_found",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_404_NOT_FOUND)

def method_not_allowed(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Method not allowed."

        ctx = {
            "status_code": status.HTTP_405_METHOD_NOT_ALLOWED,
            "message": message,
            "default_code": "method_not_allowed",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def permission_denied(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "You do not have permission to perform this action."

        ctx = {
            "status_code": status.HTTP_403_FORBIDDEN,
            "message": message,
            "default_code": "permission_denied",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_403_FORBIDDEN)

def not_authenticated(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Authentication credentials were not provided."

        ctx = {
            "status_code": status.HTTP_401_UNAUTHORIZED,
            "message": message,
            "default_code": "not_authenticated",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_401_UNAUTHORIZED)

def  authentication_failed(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Incorrect authentication credentials."

        ctx = {
            "status_code": status.HTTP_401_UNAUTHORIZED,
            "message": message,
            "default_code": "authentication_failed",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_401_UNAUTHORIZED)

def parse_error(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Malformed request."

        ctx = {
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": message,
            "default_code": "parse_error",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_400_BAD_REQUEST)

def server_error(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Internal Server Error."

        ctx = {
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": message,
            "default_code": "error",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def bad_request(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Bad Request."

        ctx = {
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": message,
            "default_code": "bad_request",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_400_BAD_REQUEST)

def conflict(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Conflict."

        ctx = {
            "status_code": status.HTTP_409_CONFLICT,
            "message": message,
            "default_code": "conflict",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_409_CONFLICT)

def unprocessable_entity(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Unprocessable Entity."

        ctx = {
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": message,
            "default_code": "unprocessable_entity",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

def unsupported_media_type(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Unsupported Media Type."

        ctx = {
            "status_code": status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            "message": message,
            "default_code": "unsupported_media_type",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

def throttled(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Throttled."

        ctx = {
            "status_code": status.HTTP_429_TOO_MANY_REQUESTS,
            "message": message,
            "default_code": "throttled",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_429_TOO_MANY_REQUESTS)

def bad_gateway(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Bad Gateway."

        ctx = {
            "status_code": status.HTTP_502_BAD_GATEWAY,
            "message": message,
            "default_code": "bad_gateway",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_502_BAD_GATEWAY)

def gateway_timeout(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Gateway Timeout."

        ctx = {
            "status_code": status.HTTP_504_GATEWAY_TIMEOUT,
            "message": message,
            "default_code": "gateway_timeout",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_504_GATEWAY_TIMEOUT)


def service_unavailable(detail=None, message=None):
        if detail is None:
            detail = "no context"
        if message is None:
            message = "Service Unavailable."

        ctx = {
            "status_code": status.HTTP_503_SERVICE_UNAVAILABLE,
            "message": message,
            "default_code": "service_unavailable",
            "detail": detail,
        }
        return http_error_handler(ctx, status=status.HTTP_503_SERVICE_UNAVAILABLE)



from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def http_error_handler(ctx, status):
    return Response(ctx, status)

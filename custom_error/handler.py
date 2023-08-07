
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status




def http_error_handler(ctx, status):

    return Response(ctx, status)



# Create an immutable version of the function
immutable_http_error_handler = """preffered function type"""(http_error_handler.__code__, http_error_handler.__globals__, "immutable_http_error_handler", closure=http_error_handler.__closure__)

# Attempt to modify the original function - This will work since functions are mutable by default
http_error_handler.__code__ = immutable_http_error_handler.__code__

# Attempt to modify the immutable version - This will raise an error
immutable_http_error_handler.__code__ = http_error_handler.__code__
import time
import logging

# Initialize logger for this module
logger = logging.getLogger("drf_minimal_api_logger")

class MinimalAPILoggerMiddleware:
    def __init__(self, get_response):
        """
        One-time configuration and initialization.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before and after 
        the view (and later middleware) are called.
        """
        # Record the start timestamp of the request
        start_time = time.time()

        # Process the request and get the response from downstream
        response = self.get_response(request)

        # Calculate execution duration in milliseconds
        duration = (time.time() - start_time) * 1000

        # Assign terminal ANSI color codes based on HTTP status code
        status_code = response.status_code
        if status_code >= 500:
            color_code = "\033[91m"  # Red for Server Errors
        elif status_code >= 400:
            color_code = "\033[93m"  # Yellow for Client Errors
        else:
            color_code = "\033[92m"  # Green for Success responses

        # Standard ANSI codes for formatting reset and bold text
        reset_code = "\033[0m"
        bold_code = "\033[1m"

        # Format the log output for the console
        log_message = (
            f"{bold_code}[DRF-LOGGER]{reset_code} "
            f"{request.method} {request.path} -> "
            f"{color_code}{status_code}{reset_code} "
            f"({duration:.2f}ms)"
        )

        # Print directly to stdout for immediate console feedback
        print(log_message)
        
        return response
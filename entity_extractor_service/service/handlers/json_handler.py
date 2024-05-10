import json
import tornado

class JSONHandler(tornado.web.RequestHandler):
    """
    Base handler class for Tornado applications, ensuring JSON responses.

    This class automatically sets the content type header to 'application/json'
    and provides helper methods for writing JSON data and handling errors with
    JSON responses.
    """

    def set_default_headers(self):
        """
        Sets the default content type header to 'application/json'.
        """
        super().set_default_headers()
        self.set_header("Content-Type", "application/json")

    def write_json(self, data):
        """
        Writes JSON data to the response.

        Args:
            data (dict or list): The data to be encoded as JSON.
        """
        self.write(json.dumps(data))

    def write_error(self, status_code, **kwargs):
        """
        Writes a JSON error response with the specified status code and message.

        Args:
            status_code (int): The HTTP status code for the error.
            **kwargs: Additional keyword arguments to be included in the JSON response.
        """
        self.set_status(status_code)
        data = {"error": kwargs.get("message", "Internal Server Error")}
        data.update(kwargs)
        self.write(json.dumps(data))

    # Handle errors in older Tornado versions
    def on_finish(self):
        if self._headers_written and self._status_code >= 400:
            # Check if an error occurred and headers were written
            exc = getattr(self, "_exc_info", None)  # Handle potential absence of _exc_info
            if exc:
                exc = exc()[1]  # Access the exception object if it exists
                self.write_error(self._status_code, exc=exc)
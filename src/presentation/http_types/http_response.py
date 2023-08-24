class HttpResponse:

    def __init__(self, status_code, body) -> None:

        self.body = body
        self.status_code = status_code

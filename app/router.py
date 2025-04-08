
from app.models import HttpRequest, HttpResponse


def handle_request(request: HttpRequest) -> HttpResponse:
    

    match request.target.split("/")[1:]:
        case [""]:
            return HttpResponse(
                status_code=200,
                headers={"Content-Type": "text/plain"},
                body="<h1>Hello, World!</h1>",
            )
        case ["echo", name]:
            return HttpResponse(
                status_code=200,
                headers={"Content-Type": "text/plain", "Content-Length": str(len(name))},
                body=f"{name}",
            )
        case _:
            return HttpResponse(
                status_code=404,
                headers={},
                body="<h1>404 Not Found</h1>",
            )

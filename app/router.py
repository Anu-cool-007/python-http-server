
from app.models import HttpRequest, HttpResponse


def handle_request(request: HttpRequest) -> HttpResponse:

    match request.target.split("/")[1:]:
        case [""]:
            return HttpResponse(
                status_code=200,
                status_text="OK",
                headers={"Content-Type": "text/plain"},
                body="<h1>Hello, World!</h1>",
            )
        case ["echo", name]:
            return HttpResponse(
                status_code=200,
                status_text="OK",
                headers={"Content-Type": "text/plain", "Content-Length": str(len(name))},
                body=f"{name}",
            )
        case ["user-agent"]:
            user_agent = request.headers['User-Agent']
            return HttpResponse(
                status_code=200,
                status_text="OK",
                headers={"Content-Type": "text/plain", "Content-Length": str(len(user_agent))},
                body=f"{user_agent}",
            )
        case _:
            return HttpResponse(
                status_code=404,
                status_text="Not Found",
                headers={},
                body="<h1>404 Not Found</h1>",
            )

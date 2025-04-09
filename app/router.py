from argparse import Namespace
import os
from pathlib import Path

from app.models import HttpRequest, HttpResponse


def handle_request(request: HttpRequest, args: Namespace) -> HttpResponse:

    match request.target.split("/")[1:]:
        case [""]:
            return HttpResponse(
                status_code=200,
                status_text="OK",
                headers={"Content-Type": "text/plain"},
                body="Hello, World!",
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
        case ["files", filename]:
            base_path = vars(args).get("directory")
            if not base_path:
                return HttpResponse(
                    status_code=500,
                    status_text="Internal Server Error",
                    headers={},
                    body="No directory specified",
                )
            path = Path(os.path.join(base_path, filename))

            if path.is_file():
                with open(path, "rb") as file:
                    content = file.read()
                return HttpResponse(
                    status_code=200,
                    status_text="OK",
                    headers={
                        "Content-Type": "application/octet-stream",
                        "Content-Length": str(len(content)),
                    },
                    body=content.decode(),
                )
            else:
                return HttpResponse(
                    status_code=404,
                    status_text="Not Found",
                    headers={},
                    body="404 Not Found",
                )
        case _:
            return HttpResponse(
                status_code=404,
                status_text="Not Found",
                headers={},
                body="404 Not Found",
            )

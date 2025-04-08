from dataclasses import dataclass


@dataclass
class HttpRequest:
    method: str
    target: str
    http_version: dict
    body: str
    query_params: dict


@dataclass
class HttpResponse:
    status_code: int
    status_text: str
    headers: dict
    body: str
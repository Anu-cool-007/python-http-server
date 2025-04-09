import gzip

from app.models import HttpRequest, HttpResponse



def decode_request(request: bytes) -> HttpRequest:
    """
    Decode the HTTP request to extract the method and path.
    """
    request_str = request.decode()
    lines = request_str.split("\r\n")
    method, path, http_version = lines[0].split(" ")
    headers = {}
    for header in lines[1:-2]:
        key, value = header.split(": ")
        headers[key] = value

    return HttpRequest(
        method=method,
        target=path,
        http_version=http_version,
        headers=headers,
        body=lines[-1],
        query_params={},
    )


def encode_response(response: HttpResponse, encoding: str) -> bytes:
    """
    Encode the HTTP response to bytes.
    """

    if encoding == "gzip":
        response.body = gzip.compress(response.body.encode())
        response.headers["Content-Encoding"] = "gzip"
        response.headers["Content-Length"] = str(len(response.body))

    status_line = f"HTTP/1.1 {response.status_code} {response.status_text}\r\n"
    headers = "".join([f"{key}: {value}\r\n" for key, value in response.headers.items()])
    body = response.body

    if isinstance(body, str):
        body = body.encode()

    return (status_line + headers + "\r\n").encode() + body


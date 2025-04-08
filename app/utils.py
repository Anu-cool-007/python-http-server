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


def encode_response(response: HttpResponse) -> bytes:
    """
    Encode the HTTP response to bytes.
    """
    status_line = f"HTTP/1.1 {response.status_code} {response.status_text}\r\n"
    headers = "".join([f"{key}: {value}\r\n" for key, value in response.headers.items()])
    body = response.body
    return (status_line + headers + "\r\n" + body).encode()


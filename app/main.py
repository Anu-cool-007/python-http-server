import socket

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
    headers: dict
    body: str


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
        body=lines[-1],
        query_params={},
    )


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
        connection, address = server_socket.accept()
        print(address)

        data = connection.recv(1024)
        request = decode_request(data)

        if request.target == "/":
            connection.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
        else:
            connection.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")


if __name__ == "__main__":
    main()

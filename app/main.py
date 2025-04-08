import socket

from app.router import handle_request
from app.utils import decode_request, encode_response


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

        response = handle_request(request)

        connection.sendall(encode_response(response))


if __name__ == "__main__":
    main()

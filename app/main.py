import socket

from app.utils import decode_request  # noqa: F401




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

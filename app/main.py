import socket
import threading

from app.router import handle_request
from app.utils import decode_request, encode_response


def handler(client_socket):
    with client_socket:
        data = client_socket.recv(1024)
        request = decode_request(data)

        response = handle_request(request)

        client_socket.sendall(encode_response(response))
        print(f"Sent response to {client_socket.getpeername()}")
        print(f"Response: {response}")
        print(f"Request: {request}")
        print(f"Headers: {request.headers}")
        print(f"Body: {request.body}")

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
        while True:
            client_soc, client_address = server_socket.accept()
            # Send each "client_soc" connection as a parameter to a thread.
            threading.Thread(target=handler,args=(client_soc,), daemon=True).start()
            print(f"Accepted connection from {client_address}")


if __name__ == "__main__":
    main()

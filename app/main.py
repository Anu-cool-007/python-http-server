import argparse
import socket
import threading

from argparse import Namespace
from socket import socket as Socket

from app.router import handle_request
from app.utils import decode_request, encode_response



def handler(client_socket: Socket, args: Namespace):
    with client_socket:
        data = client_socket.recv(1024)
        request = decode_request(data)

        response = handle_request(request, args)

        print(f"Request: {request}")
        print(f"Headers: {request.headers}")
        print(f"Body: {request.body}")
        print(f"Response: {response}")
        client_socket.sendall(encode_response(response))

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    parser=argparse.ArgumentParser()
    parser.add_argument("--directory", help="Specify the file directory")

    args = parser.parse_args()

    # Uncomment this to pass the first stage
    #
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
        while True:
            client_soc, client_address = server_socket.accept()
            # Send each "client_soc" connection as a parameter to a thread.
            print(f"Accepted connection from {client_address}")
            threading.Thread(target=handler, args=(client_soc, args), daemon=True).start()


if __name__ == "__main__":
    main()

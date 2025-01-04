import socket
import threading
import hashlib
import os
import json
import sys
import signal
from logic import already_voted


# Define server constants
SERVER_NAME = '0.0.0.0'  
SERVER_PORT = 12000
CANDIDATE_FILE = "files/candidates.txt"


global server_socket
server_socket = None


# prevent race conditions on file access
file_lock = threading.Lock()


def handle_client(client_socket, client_address):
    try:
        print(f"Connection from {client_address} established")

        # message recieved
        message = client_socket.recv(1024).decode()
        if not message:
            return

       
        try:
            # process the message
            data = json.loads(message)
            client_id = data.get('client_id')

            # check if the user already votes or not [can be removed while debugging]
            if already_voted(client_id):
                client_socket.sendall(b"You already voted!")
                client_socket.close()  
                return

            vote = data.get('vote')

        # if message format was wrong, as in a non-JSON format
        except json.JSONDecodeError:
            client_socket.sendall(b"Invalid message format")
            client_socket.close()  
            return

        # add file to the votes.txt
        with file_lock:
            process_vote(client_id, vote)

      
        response = f"Vote for {vote} has been recorded successfully!"
        client_socket.sendall(response.encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client socket
        client_socket.close()





# add votes to votes.txt
def process_vote(client_id, vote):

    vote_filename = "votes.txt"

    with open(vote_filename, "a") as file:
        file.write(f"{client_id}: {vote}\n")
    print(f"Vote recorded: {client_id} voted {vote}")

    
# Function to start the server and listen for incoming client connections
def start_server():
    global server_socket
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # i can reuse the address

    # Bind the socket to the address and port
    server_socket.bind((SERVER_NAME, SERVER_PORT))
    print(f"Server started on {SERVER_NAME}:{SERVER_PORT}")

    # Start listening for incoming connections (max 5 connections in the backlog)
    server_socket.listen(5)
    running = True
    # Continuously accept and handle client connections
    while running:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.daemon = True
        client_thread.start()
    



def shutdown_server():
    global server_socket
    print("Shutting down server...")
    if server_socket:
        server_socket.close()
    


if __name__ == "__main__":
    if not os.path.exists("files"):
        os.makedirs("files")
    if not os.path.exists(CANDIDATE_FILE):
        with open(CANDIDATE_FILE, "w") as f:
            pass  # Create the file if it doesn't exist
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown_server())
    start_server()
